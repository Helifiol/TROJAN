import socket

HOST = "127.0.0.1"
PORT = 40000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("socket created")
    s.listen(5)
    print("socket listening")

    while True:
        c, addr = s.accept()
        print(f"the IP of the web server is {addr[0]} on port 8020")
        data = c.recv(1024).decode()
        print(data)
        c.close()