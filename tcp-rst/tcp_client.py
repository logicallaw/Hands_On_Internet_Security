import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8888))
    print("Connected to server.")

    try:
        while True:
            s.sendall(b"hello")
            data = s.recv(1024)
            print("Server:", data.decode())
            time.sleep(1)
    except Exception as e:
        print("Client disconnected:", e)