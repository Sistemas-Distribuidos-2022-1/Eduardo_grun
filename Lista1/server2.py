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

    nome,sexo,idade = data.split('_')


    idade = int(idade)

    if idade >= 18 and (sexo == 'M' or sexo == 'O'):
        msg = 'Maioridade atingida'
    elif idade >= 21 and sexo == 'F':
        msg = 'Maioridade atingida'
    else:
        msg = 'Maioridade não atingida'

    #data = str.encode(msg)
    data = str.encode(msg)
    conn.sendall(data)