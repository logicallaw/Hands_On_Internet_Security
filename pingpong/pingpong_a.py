import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))

while True:
    data, addr = sock.recvfrom(1024)
    print(f"A got from {addr}: {data.decode().strip()}")
    sock.sendto(b'A says pong!\n', addr)