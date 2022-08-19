import rpyc
import time, random

try:
    c = rpyc.connect(None,8080)
except ConnectionRefusedError:
    print(ConnectionRefusedError.errno)
    exit()

while True:
    id = random.randint(1,1000)
    c.root.produce(id)
    print(f'Produziu {id}')
    time.sleep(5)
    