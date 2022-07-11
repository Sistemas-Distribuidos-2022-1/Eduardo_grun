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

    alt,sexo = data.split('_')
    alt = float(alt)

    if sexo == 'M' or sexo == 'O':
        peso = (72.7 * alt) - 58
    else:
        peso = (62.1 * alt) - 44.7

    msg = str(peso)
 
    data = str.encode(msg)
    conn.sendall(data)