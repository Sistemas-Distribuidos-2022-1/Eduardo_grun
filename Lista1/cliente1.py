import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Nome: ")
nome = input()
print("Cargo: ")
car = input()
print("Sal: ")
sal = input()

msg = str(nome + '_' + car + '_' + sal)

s.sendall(str.encode(msg))

data = s.recv(1024)

data = data.decode()
nome,car,sal = data.split('_') 
print('Nome: ', nome)
print('Cargo: ', car)
print('Reajuste: ', sal)
