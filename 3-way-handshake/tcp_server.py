import socket

HOST = '0.0.0.0'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"TCP server listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"Accepted connection from {addr}")
        conn.sendall(b"Hello from server\n")
        conn.close()