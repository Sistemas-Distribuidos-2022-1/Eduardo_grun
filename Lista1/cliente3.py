import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("N1:")
n1 = input()
print("N2")
n2 = input()
print("N3")
n3 = input()

msg = str(n1 + '_' + n2 + '_' + n3)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()
print(data)
