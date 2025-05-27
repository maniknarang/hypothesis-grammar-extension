import ipaddress
from pathlib import Path
import subprocess
import unittest

from hypothesis import given, strategies as st

def setup():
    '''
        Run grammarinator to create for the g4 file and generate samples for testing
    '''
    parent_path = Path(__file__).parent

    subprocess.run(['grammarinator-process', str(parent_path) + '/ConvertedGrammar.g4',
                    '-o', str(parent_path), '--no-actions'],
                    check=True)

    ipv4_samples = subprocess.run(['grammarinator-generate',
                              'ConvertedGrammarGenerator.ConvertedGrammarGenerator',
                              '-r', 'ipv4', '-n', '100', '-d', '20', '--sys-path', str(parent_path), '--stdout'],
                              capture_output=True, text=True, check=True)
    ipv4_samples = [line.strip() for line in ipv4_samples.stdout.splitlines() if line.strip()]

    ipv6_samples = subprocess.run(['grammarinator-generate',
                              'ConvertedGrammarGenerator.ConvertedGrammarGenerator',
                              '-r', 'ipv6', '-n', '100', '-d', '20', '--sys-path', str(parent_path), '--stdout'],
                              capture_output=True, text=True, check=True)
    ipv6_samples = [line.strip() for line in ipv6_samples.stdout.splitlines() if line.strip()]

    return ipv4_samples, ipv6_samples

# Hypothesis strategy to choose inputs from samples
test_ipv4_samples, test_ipv6_samples = setup()
print(test_ipv4_samples, test_ipv6_samples)
sample_ipv4_strategy, sample_ipv6_strategy = st.sampled_from(test_ipv4_samples), st.sampled_from(test_ipv6_samples)

class TestIp(unittest.TestCase):
    @given(sample_ipv4_strategy)
    def test_ipv4_inverse(self, ip):
        print('Generated IPv4', ip)
        ip_address = ipaddress.IPv4Address(ip)
        assert str(ip_address) == ip

    @given(sample_ipv6_strategy)
    def test_ipv6_inverse(self, ip):
        print('Generated IPv6', ip)
        ip_address = ipaddress.IPv6Address(ip)
        assert ipaddress.IPv6Address(ip) == ipaddress.IPv6Address(str(ip_address))

    @given(sample_ipv4_strategy)
    def test_ipv4_in_range(self, ip):
        print('Generated IPv4', ip)
        octets = str(ip).split('.')
        for octet in octets:
            assert 0 <= int(octet) <= 255
        assert len(octets) == 4

    @given(sample_ipv6_strategy)
    def test_ipv6_hextet_format(self, ip):
        print('Generated IPv6', ip)
        hextets = str(ip).split(':')
        for hectet in hextets:
            for char in hectet:
                assert char.lower() in '0123456789abcdef'
        assert len(hextets) == 8