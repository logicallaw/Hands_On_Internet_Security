# victim.py
import socket
import time

s = socket.socket()
s.connect(("127.0.0.1", 9090))  # 서버에 연결
print("🙋‍♂️ victim connected to server")

while True:
    s.send(b"hello from victim\n")
    time.sleep(7)