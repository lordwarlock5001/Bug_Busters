import socket
s=socket.socket()
name=socket.gethostname()
s.bind((name,12345))
s.listen(5)
print(name)
while True:
    c,add=s.accept()
    print(add[0])
    print("in While")
    c.send(bytes("connected",'utf-8'))
    c.close()