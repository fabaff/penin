"""Support for creating ICMP requests."""
from scapy.all import ICMP, IP, TCP, sr, sr1


def create_icmp_request(destination, icmp_type):
    """Create an ICMP request."""
    response = sr1(
        IP(dst=str(destination)) / ICMP(type=icmp_type), timeout=2, verbose=0
    )

    if response is None:
        return None

    if int(response.getlayer(ICMP).type) == 14:
        return "Timestamp replay"

    if int(response.getlayer(ICMP).type) == 0:
        return "Echo replay"
