# coding=utf-8
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import zmq


context = zmq.Context()

#  Socket to talk to server
print("Connecting to Pepper's server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
message = "Received"
#  Do 10 requests, waiting each time for a response
while message=="Received":
    print("Sending request")
    predicates= raw_input ('Can you tell me predicates that you want to add? Put them into parenthesis, please ')
    socket.send(predicates)
    #  Get the reply.
    message = socket.recv()
    print(message)
exit (0)