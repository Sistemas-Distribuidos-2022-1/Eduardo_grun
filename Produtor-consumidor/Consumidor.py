import rpyc,time

try:
    c = rpyc.connect(None,8080)
except ConnectionRefusedError:
    print(ConnectionRefusedError.errno)
    exit()

while True:
    id = c.root.consume()
    print(f'Consumido {id}')
    time.sleep(1)

    
