from scapy import *
p = IP ('dst=192.168.2.12')/ICMP()
p[ICMP].type = 8
q = srl(p)
q.show()
