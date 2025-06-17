# udp_listener.py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12345))  # localhost만 수신
print("Listening on UDP port 12345...")

while True:
    data, addr = sock.recvfrom(4096)
    print(f"[+] Received from {addr}: {data.decode(errors='ignore')}")
