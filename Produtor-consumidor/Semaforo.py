from numpy import empty
import rpyc,threading

limit = 10

buffer = []
full = threading.Semaphore(limit)
empty = threading.Semaphore(limit)

class BufferService(rpyc.Service):
    def exposed_produce(self,id):
        full.acquire()
        buffer.append(id)
        empty.release()
        print(f'Produced {id}, tamanho = {len(buffer)}')

    def exposed_consume(self):
        empty.acquire()
        id = buffer.pop(0)
        full.release()
        print(f'Consumed {id}, tamanho = {len(buffer)}')
        return id

for i in range(limit):
    empty.acquire()

server = rpyc.ThreadedServer(BufferService, port=8080)
server.start()