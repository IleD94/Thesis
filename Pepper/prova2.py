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
    goal = raw_input ('Can you give me my goal please, for example isHappy Robot: ')
    personality = raw_input ('Can you give me my personality please, for example isHappy Robot: ')
    language= raw_input ('Can you give me my language please, for example isHappy Robot: ')
    msg = "{},{},{}".format(goal, personality, language)
    socket.send_string(msg)
    #  Get the reply.
    message = socket.recv()
    print(message)

exit (0)