import ipytest
import ipaddress
from hypothesis import given
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "hypothesis_cfg")),
)

from hypothesis_cfg import cfg  # type: ignore

@given(cfg("tests/ip/cfgs/ip.cfg", max_depth=20))
def test_ip_inverse(ip: str):
    print('Generated IP: ', ip)
    if ':' in ip:
        ip_address = ipaddress.IPv6Address(ip)
        assert ipaddress.IPv6Address(ip) == ipaddress.IPv6Address(str(ip_address))
    elif '.' in ip:
        ip_address = ipaddress.IPv4Address(ip)
        assert str(ip_address) == ip

@given(cfg("tests/ip/cfgs/ip.cfg", max_depth=20))
def test_ip_in_range(ip: str):
    print('Generated IP', ip)
    if ':' in ip:
        hextets = str(ip).split(':')
        for hectet in hextets:
            for char in hectet:
                assert char.lower() in '0123456789abcdef'
        assert len(hextets) == 8
    elif '.' in ip:
        octets = str(ip).split('.')
        for octet in octets:
            assert 0 <= int(octet) <= 255
        assert len(octets) == 4

ipytest.run("-s")