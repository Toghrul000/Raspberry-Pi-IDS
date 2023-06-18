from scapy.all import *

payload = "A" * 1000

# Craft the IP packet
ip_packet = IP(dst="192.168.178.81")

# Craft the TCP packet
tcp_packet = TCP(sport=1234, dport=80, flags="S", seq=12345, ack=1000)

# Combine IP and TCP packets with payload
packet = ip_packet / tcp_packet / payload

# Send the packet
send(packet)
