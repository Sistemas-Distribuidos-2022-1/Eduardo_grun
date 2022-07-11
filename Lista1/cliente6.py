import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

print("Nome:")
nome = input()
print("Nivel:")
nivel = input()
print("Salario:")
salario = input()
print("Número de dependentes:")
ndep = input()

msg = str(nome + '_' + nivel + '_' + salario + '_' + ndep)

s.sendall(str.encode(msg))

data = s.recv(1024)
data = data.decode()
nome,nivel,salario,ndep = data.split('_')

print('Nome:', nome)
print('Nivel:', nivel)
print('Salario:', salario)
print('Número de dependentes:', ndep)
