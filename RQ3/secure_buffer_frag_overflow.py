from scapy.all import *

payload = "A" * 1000

# Craft the IP packet
ip_packet = IP(dst="localhost")

# Fragment the TCP packet into smaller fragments
tcp_packet = TCP(sport=1234, dport=8080, flags="S", seq=12345, ack=1000)
fragments = fragment(ip_packet / tcp_packet / payload, fragsize=100)

# Send the fragments through the SSH tunnel
for fragment in fragments:
    send(fragment, verbose=True)
