import rpyc, threading

limit = 20
buffer = []
producer = threading.Lock()
consumer = threading.Lock()
consumer.acquire()

class BufferService(rpyc.Service):
    def exposed_produce(self,id):
        producer.acquire()
        buffer.append(id)
        
        if consumer.locked():
            consumer.release()
        
        if len(buffer) < limit:
            producer.release()
        
        print(f"Produced = {id}, tamanho do buffer = {len(buffer)}")
    
    def exposed_consume(self):
        consumer.acquire()
        id = buffer.pop(0)

        if producer.locked():
            producer.release()
        
        if len(buffer) > 0:
            consumer.release()
        
        print(f'Consumed {id}, tamanho do buffer = {len(buffer)}')

        return id

server = rpyc.ThreadedServer(BufferService, port=8080)
server.start()