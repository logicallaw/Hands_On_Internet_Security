#!/usr/bin/env python3
from scapy.all import *

def spoof_pkt(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:  # Echo Request
        print("[*] Original Packet")
        print("    Source IP:", pkt[IP].src)
        print("    Destination IP:", pkt[IP].dst)

        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
        data = pkt[Raw].load if Raw in pkt else b''

        newpkt = ip / icmp / data

        print("[*] Spoofed Reply Sent")
        print("    Source IP:", newpkt[IP].src)
        print("    Destination IP:", newpkt[IP].dst)

        send(newpkt, verbose=0)

# 루프백(내 컴퓨터 자신)에서 오는 ICMP 요청만 감지
sniff(filter="icmp and src host 127.0.0.1", iface="lo0", prn=spoof_pkt)
