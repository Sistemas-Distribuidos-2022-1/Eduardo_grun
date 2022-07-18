# cliente

import zmq

#HOST = '192.168.40.81'
#PORT = 15000

context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://192.168.40.81:5555"  # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "TIM") # subscribe to TIME messages

for i in range(5): # Five iterations
	time = s.recv() # receive a message
	print(time)
