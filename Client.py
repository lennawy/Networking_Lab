import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 20213))
msg = b"This is a test from python client"  # transfer into byte
s.send(msg)

data, addr = s.recvfrom(1024)
print(data.decode('utf-8'))

s.close
