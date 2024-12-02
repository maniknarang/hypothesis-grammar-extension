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


def is_valid_http_request(request):
    # split request into lines
    lines = request.split("\r\n")

    # needs at least request line + headers
    if len(lines) < 2:
        return False

    # validate request line
    request_line = lines[0]
    request_line_pattern = r"^(GET|POST|PUT) \S+ HTTP/1\.[01]$"
    if not re.match(request_line_pattern, request_line):
        return False

    # validate header format
    headers = lines[1:]
    for header in headers:
        if header == "":
            break
        if not re.match(r"^[\w-]+: .+$", header):  # key: value
            return False

    return True


@given(cfg("tests/http/cfgs/httprequest.cfg", max_depth=50))
def test_http_request_format(http_request):
    assert is_valid_http_request(http_request)


@given(cfg("tests/http/cfgs/httprequest.cfg", max_depth=50))
def test_http_request_format_invalid(http_request):
    for replace_string in ["GET", "POST", "PUT"]:
        http_request = http_request.replace(replace_string, "INVALID", 1)
    assert not is_valid_http_request(http_request)


@given(cfg("tests/http/cfgs/httprequest.cfg", max_depth=50))
def test_http_request_mandatory_headers(http_request):
    # split request into lines
    lines = http_request.split("\r\n")

    # check if request is valid
    if not is_valid_http_request(http_request):
        return

    # extract headers
    headers = lines[1:]
    headers_dict = {}
    for header in headers:
        if header == "":
            break
        key, value = header.split(":", 1)
        headers_dict[key.strip()] = value.strip()

    # assert mandatory headers
    assert (
        "Host" in headers_dict
    ), "Only 'Host' is required in HTTP/1.0 and HTTP/1.1 requests"


@given(cfg("tests/http/cfgs/httprequest.cfg", max_depth=50))
def test_http_request_valid_methods_and_versions(http_request):
    # split request into lines
    lines = http_request.split("\r\n")

    # check if request is valid
    if not is_valid_http_request(http_request):
        return

    # extract request line
    request_line = lines[0]

    # validate method and version
    method, _, version = (
        request_line.partition(" ")[0],
        request_line.partition(" ")[1],
        request_line.rpartition(" ")[2],
    )

    # assert method is valid
    valid_methods = {"GET", "POST", "PUT"}
    assert method in valid_methods, f"Invalid HTTP method: {method}"

    # assert version is valid
    valid_versions = {"HTTP/1.0", "HTTP/1.1"}
    assert version in valid_versions, f"Invalid HTTP version: {version}"


ipytest.run("-s")
