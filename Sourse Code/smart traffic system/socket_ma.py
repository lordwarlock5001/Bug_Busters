import socket
class Socket_client:
    def __init__(self):
        self.ip=socket.gethostbyname(socket.gethostname())
        self.uni_id=1245
        s = socket.socket()
        port = 12345
        s.connect((socket.gethostname(), port))
        print(s.recv(1024))
        s.close()


def call_s():
    obj=Socket_client()

