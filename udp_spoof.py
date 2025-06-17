# udp_spoof.py
from scapy.all import *

spoofed_src_ip = "1.2.3.4"          # 아무 IP나 가능 (가짜 IP)
dst_ip = "127.0.0.1"             # 수신자 (내 컴퓨터)
dst_port = 12345

payload = "Spoofed packet here!"

ip = IP(src=spoofed_src_ip, dst=dst_ip) 

udp = UDP(sport=5555, dport=dst_port)

data = Raw(load=payload)

packet = ip / udp / data

packet.show()

send(packet, count=1)
