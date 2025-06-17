import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server listening on port", PORT)

    conn, addr = s.accept()
    print(f"Accepted connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Connection closed.")
                break
            print("Received:", data.decode())
            conn.sendall(b"Echo: " + data)
    except Exception as e:
        print("Error:", e)