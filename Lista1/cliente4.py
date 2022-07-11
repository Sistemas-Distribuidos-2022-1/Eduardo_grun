import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Altura:")
alt = input()
print("Sexo (M), (F) ou (O)")
sexo = input()


msg = str(alt + '_' + sexo)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()
print(data)
