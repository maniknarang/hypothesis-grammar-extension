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


def is_valid_post_request(request):
    print(request)

    # split request into lines
    lines = request.split("\r\n")

    # needs at least request line + headers + body
    if len(lines) < 3:
        return False

    # validate request line
    request_line = lines[0]
    request_line_pattern = r"^POST \S+ HTTP/1\.[01]$"
    if not re.match(request_line_pattern, request_line):
        return False

    # validate header format
    headers = lines[1:]
    body_start_index = 0
    for i, header in enumerate(headers):
        if header == "":
            body_start_index = i + 1
            break
        if not re.match(r"^[\w-]+: .+$", header):  # key: value
            return False

    # validate body
    body = "\r\n".join(headers[body_start_index:])
    if not body.strip():
        return False

    return True


@given(cfg("tests/http/cfgs/httprequest_post.cfg", max_depth=50))
def test_post_request_format(post_request):
    assert is_valid_post_request(post_request)


@given(cfg("tests/http/cfgs/httprequest_post.cfg", max_depth=50))
def test_post_request_format_invalid(post_request):
    # replace POST with invalid method and check
    post_request = post_request.replace("POST", "INVALID", 1)
    assert not is_valid_post_request(post_request)


@given(cfg("tests/http/cfgs/httprequest_post.cfg", max_depth=50))
def test_post_request_mandatory_headers(post_request):
    # split request into lines
    lines = post_request.split("\r\n")

    # check if request is valid
    if not is_valid_post_request(post_request):
        return

    # get headers
    headers = lines[1:]
    headers_dict = {}
    print(headers)
    for header in headers:
        if header == "":
            break
        key, value = header.split(":", 1)
        headers_dict[key.strip()] = value.strip()

    # assert mandatory headers
    assert "Host" in headers_dict, "'Host' header is required"
    assert "Content-Type" in headers_dict, "'Content-Type' header is required"
    assert "Content-Length" in headers_dict, "'Content-Length' header is required"


@given(cfg("tests/http/cfgs/httprequest_post.cfg", max_depth=50))
def test_post_request_valid_versions(post_request):
    # split request into lines
    lines = post_request.split("\r\n")

    # check if request is valid
    if not is_valid_post_request(post_request):
        return

    # get request line
    request_line = lines[0]

    # validate version
    version = request_line.rpartition(" ")[2]
    print(version)
    valid_versions = {"HTTP/1.0", "HTTP/1.1"}
    assert version in valid_versions, f"Invalid HTTP version: {version}"


@given(cfg("tests/http/cfgs/httprequest_post.cfg", max_depth=50))
def test_post_request_body_present(post_request):
    # split request into lines
    lines = post_request.split("\r\n")

    # valid request
    if not is_valid_post_request(post_request):
        return

    # check body
    body_start_index = 0
    for i, line in enumerate(lines):
        if line == "":
            body_start_index = i + 1
            break

    body = "\r\n".join(lines[body_start_index:])
    assert body.strip(), "POST requests must have a non-empty body"


ipytest.run("-s")
