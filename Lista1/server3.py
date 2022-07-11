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

    n1,n2,n3 = data.split('_')
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    m = (n1+n2)/2

    if m >= 7:
        msg = 'Aprovado!'
    elif m >= 3 and m < 7:
        if (m+n3)/2 >= 5:
            msg = 'Aprovado"'
        else:
            msg = 'Reprovado!'
    else:
        msg = 'Reprovado!'

    data = str.encode(msg)
    conn.sendall(data)