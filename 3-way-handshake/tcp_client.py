import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8888)) 
    msg = s.recv(1024)
    print(msg.decode())