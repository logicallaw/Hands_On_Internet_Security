from scapy.all import *

target_ip = "127.0.0.1"
target_port = 8888
src_port = RandShort()

# 1. SYN 보내기
ip = IP(dst=target_ip)
syn = TCP(sport=src_port, dport=target_port, flags="S", seq=1000)
syn_ack = sr1(ip/syn, timeout=1, verbose=0)

if syn_ack and syn_ack.haslayer(TCP) and syn_ack[TCP].flags == "SA":
    print("[+] SYN-ACK received.")

    # 2. ACK 보내기
    ack = TCP(sport=src_port, dport=target_port,
              flags="A",
              seq=syn_ack.ack,
              ack=syn_ack.seq + 1)
    send(ip/ack, verbose=0)
    print("[+] ACK sent. 3-way handshake complete.")
else:
    print("[-] No SYN-ACK received. Server not responding.")