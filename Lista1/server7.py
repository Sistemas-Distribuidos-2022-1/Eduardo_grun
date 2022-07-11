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

    idade,anos = data.split('_')
    idade = int(idade)
    anos = int(anos)

    if idade >= 65:
        msg = 'Pode se aposentar'
    elif anos >= 30:
        msg = 'Pode se aposentar'
    elif idade >= 60 and anos >= 25:
        msg = 'Pode se aposentar'
    else:
        msg = 'Não pode se aposentar'
    
    data = str.encode(msg)
    conn.sendall(data)