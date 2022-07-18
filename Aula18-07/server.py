import zmq, time

#HOST = '192.168.40.81'
#PORT = 15000

context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = "tcp://*:5555" # how and where to communicate
s.bind(p) # bind socket to the address

while True:
	time.sleep(5) # wait every 5 seconds
	s.send_string("TIME_Eduardo" + time.asctime()) # publish the current time
