import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Idade:")
age = input()

msg = str(age)

s.sendall((msg+'\n').encode())

data = s.recv(1024)

data = data.decode()
print(data)