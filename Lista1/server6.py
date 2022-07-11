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

    nome,nivel,salario,ndep = data.split('_')
    salario = float(salario)
    ndep = int(ndep)

    if nivel == 'A':
        if ndep > 0:
            salario = salario * 0.97
        else:
            salario = salario * 0.92
    elif nivel == 'B':
        if ndep > 0:
            salario = salario * 0.95
        else:
            salario = salario * 0.90
    elif nivel == 'C':
        if ndep > 0:
            salario = salario * 0.92
        else:
            salario = salario * 0.85
    elif nivel == 'D':
        if ndep > 0:
            salario = salario * 0.90
        else:
            salario = salario * 0.83

    msg = str(nome + '_' + nivel + '_' + str(salario) + '_' + str(ndep))
    data = str.encode(msg)
    conn.sendall(data)