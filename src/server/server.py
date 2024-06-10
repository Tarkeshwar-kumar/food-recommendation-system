import socket



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("localhost", 5000))

    server.listen()
    conn, addr = server.accept()
    with conn:

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)