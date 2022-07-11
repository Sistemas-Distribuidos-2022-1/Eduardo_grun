import socket

HOST = 'localhost'
PORT =  10000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

print('Aguardando conexão ')
conn, ender = s.accept()

print('Conectado em: ', ender)

while True:
	data = conn.recv(2048)	
	
	if not data:
		print('Fechando conexão')
		conn.close()
		break	
	
	data = data.decode()

	nome,car,sal = data.split('_')

	sal = float(sal)
	
	if car == 'operador':
		sal *= 1.2
	if car == 'programador':
		sal *= 1.18
	
	data = str.encode(nome + '_' + car + '_' + str(sal))
	
	conn.sendall(data)