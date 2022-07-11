import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Idade:")
idade = input()
print("Anos de serviço:")
anos = input()

msg = str(idade + '_' + anos)

s.sendall(str.encode(msg))

data = s.recv(1024)
data = data.decode()
print(data)