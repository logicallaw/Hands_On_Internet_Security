import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9999))

# 응답 메시지 - 큰 데이터로 구성 (예: 5000바이트)
large_response = b"A" * 5000

print("Amplifiable UDP server is running on port 9999...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data}")
    sock.sendto(large_response, addr)