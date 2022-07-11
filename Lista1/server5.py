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

    age = int(data)

    if age >= 5 and age <= 7:
        msg = 'Infantil A'
    elif age >= 8 and age <= 10:
         msg = 'Infantil B'
    elif age >= 11 and age <= 13:
         msg = 'Juvenil A'
    elif age >= 14 and age <= 17:
         msg = 'Juvenil B'
    elif age >= 18 :
         msg = 'Adulto'
    else:
         msg = 'Idade inválida'
 
    data = str.encode(msg)
    conn.sendall(data)