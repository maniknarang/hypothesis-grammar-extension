import math
import ipytest
from hypothesis import given
import sys
import os
import re

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore


def is_valid_get_request(request):
    print(request)

    # split request into lines
    lines = request.split("\r\n")

    # needs at least request line + headers
    if len(lines) < 2:
        return False

    # validate GET request line
    request_line = lines[0]
    request_line_pattern = r"^GET /[A-Za-z0-9_/]* HTTP/1\.[01]$"
    if not re.match(request_line_pattern, request_line):
        return False

    # validate headers format
    headers = lines[1:]
    for header in headers:
        if header == "":
            break
        if not re.match(r"^[\w-]+: .+$", header):  # key: value
            return False

    return True


@given(cfg("tests/http/cfgs/httprequest_get.cfg", max_depth=50))
def test_get_request_format(get_request):
    assert is_valid_get_request(get_request)


@given(cfg("tests/http/cfgs/httprequest_get.cfg", max_depth=50))
def test_get_request_invalid_method(get_request):
    # replace GET with an invalid method and check
    get_request = get_request.replace("GET", "INVALID", 1)
    assert not is_valid_get_request(get_request)


@given(cfg("tests/http/cfgs/httprequest_get.cfg", max_depth=50))
def test_get_request_mandatory_headers(get_request):
    # split request into lines
    lines = get_request.split("\r\n")

    # check if request is valid
    if not is_valid_get_request(get_request):
        return

    # get headers
    headers = lines[1:]
    print(headers)
    headers_dict = {}
    for header in headers:
        if header == "":
            break
        key, value = header.split(":", 1)
        headers_dict[key.strip()] = value.strip()

    # assert mandatory headers
    assert "Host" in headers_dict, "'Host' header is required"
    assert "User-Agent" in headers_dict, "'User-Agent' header is required"
    assert "Accept" in headers_dict, "'Accept' header is required"


@given(cfg("tests/http/cfgs/httprequest_get.cfg", max_depth=50))
def test_get_request_valid_versions(get_request):
    # split request into lines
    lines = get_request.split("\r\n")

    # check if request is valid
    if not is_valid_get_request(get_request):
        return

    # get request line
    request_line = lines[0]

    # validate http version
    version = request_line.rpartition(" ")[2]
    print(version)
    valid_versions = {"HTTP/1.0", "HTTP/1.1"}
    assert version in valid_versions, f"Invalid HTTP version: {version}"


ipytest.run("-s")
