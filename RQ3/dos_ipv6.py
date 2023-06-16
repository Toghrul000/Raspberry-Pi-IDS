from scapy.all import *

z = "Q" * 30
send(IPv6(dst="2001:1c06:1b0e:2600:9dd4:ce94:b17e:9ab4")/ICMPv6EchoRequest(data=z), loop=1)


