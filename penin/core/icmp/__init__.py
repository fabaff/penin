"""Support for creating ICMP requests."""
from scapy.all import ICMP, IP, sr1, TCP
from scapy.all import sr, IP, ICMP


def create_icmp_request(destination, icmp_type):
    """Create an ICMP request."""
    response = sr1(IP(dst=str(destination)) / ICMP(type=icmp_type), timeout=2, verbose=0)

    if response is None:
        return None

    if int(response.getlayer(ICMP).type) == 14:
        return "Timestamp replay"

    if int(response.getlayer(ICMP).type) == 0:
        return "Echo replay"


#def make_ping_sweep(destination):
    #"""Perform a ping sweep in a given network."""
    # address_range = IPv4Network(destination)
    # live = offline = blocked = []
    #
    # for host in address_range:
    #     print("---------------------------")
    #     print("1111", len(offline))
    #     print("1111", len(live))
    #
    #     if host in (address_range.network_address, address_range.broadcast_address):
    #         # Skip network and broadcast addresses
    #         continue
    #
    #     response = sr1(IP(dst=str(host)) / ICMP(), timeout=2, verbose=0)
    #
    #     print(response)
    #
    #     print(response.getlayer(ICMP))
    #
    #     if response is None:
    #         print(f"{host} is down or not responding.")
    #         offline.append(str(host))
    #     elif (
    #             int(response.getlayer(ICMP).type) == 3 and
    #             int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
    #     ):
    #         print(f"{host} is blocking ICMP.")
    #         blocked.append(str(host))
    #     else:
    #         print(f"{host} is responding.")
    #         live.append(str(host))
    #
    #     print("222", len(offline))
    #     print(len(blocked))
    #     print(len(live))
    #
    # result = {'live': live, 'offline': offline, 'blocked': blocked}
    # print(len(result['live']))
    # print(len(result['offline']))
    # print(len(result['blocked']))
    #
    # print(result)
    #




# https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping
# https://www2.mmu.ac.uk/media/mmuacuk/content/documents/school-of-computing-mathematics-and-digital-technology/blossom/PythonScriptingwithScapyLab.pdf
#
#
#  response = sr1(IP(dst=str('192.168.0.104')) / ICMP(), timeout=2, verbose=0)
# response[0].summary()
# response.getlayer(ICMP)
# response.getlayer(ICMP).type
#
# response = sr1(IP(dst=str('192.168.0.1')) / ICMP(type=13), timeout=2, verbose=0)