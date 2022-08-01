import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Nome: ")
nome = input()
print("Sexo (M), (F) ou (O): ")
sexo = input()
print("Idade: ")
idade = input()

msg = str(nome + '_' + sexo + '_' + idade)

s.sendall((msg+'\n').encode())

data = s.recv(1024)

data = data.decode()
print(data)