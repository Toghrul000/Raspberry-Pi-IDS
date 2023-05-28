from scapy.all import *
import random

dst_ip = "192.168.178.81"

# Define the packets to send
udp_packet = IP(dst=dst_ip) / UDP(dport=5000) / Raw(load=RandBin(size=random.randint(64, 500)))
tcp_packet = IP(dst=dst_ip) / TCP(dport=5000) / Raw(load=RandBin(size=random.randint(64, 500)))
icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load=RandBin(size=random.randint(32, 128)))
dns_packet = IP(dst=dst_ip) / UDP(sport=53, dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
http_packet = IP(dst=dst_ip) / TCP(dport=5000) / Raw(load="GET / HTTP/1.1\r\nHost: {}:{}\r\n\r\n".format(dst_ip, 5000))




# Send the packets continuously
while True:
    sendp(udp_packet / tcp_packet / icmp_packet / dns_packet / http_packet)
    time.sleep(random.uniform(0.001, 0.1))
