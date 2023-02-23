# coding=utf-8
import zmq

def write_pddl (predicates, goal, myobj1):
    
    prob1 = "(define \n    (problem thesis_problem3)\n    (:domain"
    test_dom="thesis_domain3"
    mydom =  " "+ test_dom +") \n "
    prob2 = """   (:objects \n        box1 - thing\n        box2 - thing
        ball - thing\n        emptySpace - thing\n        room - place
        elsewhere - place\n        start - id \n        end - id \n        t1 - id
        t2 - id \n        t3 - id \n        t4 - id \n        t5 - id
        t6 - id \n        t7 - id \n        t8 - id
        t9 - id \n        t10 - id \n        t11 - id
        t12 - id \n        t13 - id \n        t14 - id
        t15 - id \n        t16 - id \n        t17 - id
        t18 - id \n        t19 - id \n        t20 - id
        t21 - id \n        t22 - id \n        t23 - id\n"""

    #ricordarsi di aggiungere anche gli altri oggetti, magari da sensore con i marker. Vedere come fare ##########################
    prob3 = "    \n)\n    (:init\n"
    #predicates = queue1.get()
    m=''.join([str(predicate) for predicate in predicates])
    myin = ("        "+ "\n    )\n"  )    

    prob4 = "    (:goal (and\n"

    mygoal= "        ("+str(goal)+  ")"  
            
    prob5= "\n    )  \n)    \n)"

    problem = prob1+mydom+prob2+myobj1+prob3+m+myin+prob4+mygoal+prob5
    #print (problem) 
    # Write PDDL files    
    with open("problem_created.pddl", "w") as f:
        f.write(problem)

def socket_goal_exchange ():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    goal = socket.recv()
    print("Received request: %s" % goal)
    # socket.send(b"Received")
    #  Send reply back to client
    socket.send(b"Received")
    return goal

def socket_predicates_exchange (response):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    predicates = socket.recv()
    print("Received request: %s" % predicates)
    # socket.send(b"Received")
    #  Send reply back to client
    socket.send(b"Received")
    return predicates