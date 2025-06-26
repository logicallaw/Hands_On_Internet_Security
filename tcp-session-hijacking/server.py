import socket

s = socket.socket()
s.bind(("0.0.0.0", 9090))
s.listen(1)
print("✅ 서버 대기 중...")

conn, addr = s.accept()
print(f"🔗 연결됨: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"📥 수신: {data.decode().strip()}")