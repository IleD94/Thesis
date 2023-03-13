# coding=utf-8
import zmq

def write_pddl (predicates, goal, myobj1):
    
    prob1 = "(define \n    (problem official_problem)\n    (:domain"
    test_dom="official_domain"
    mydom =  " "+ test_dom +") \n "
    prob2 = """   (:objects \n
    box1 - thing
    box2 - thing
    emptySpace - thing
    ball - thing
    room - place
    elsewhere - place

    end - id
    t1 - id
    t2 - id
    t3 - id
    t4 - id
    t5 - id
    t6 - id
    t7 - id
    t8 - id
    t9 - id
    t10 - id
    t11 - id 
    t12 - id
    t13 - id
    t14 - id
    t15 - id
    t16 - id
    t17 - id
    t18 - id
    t19 - id
    t20 - id
    t21 - id
    t22 - id
    t23 - id
    t24 - id
    t25 - id
    t26 - id
    t27 - id
    t28 - id
    t29 - id
    t30 - id
    t31 - id
    t32 - id
    t33 - id
    t34 - id
    t35 - id
    t36 - id
    t37 - id
    t38 - id
    t39 - id
    t40 - id
    t41 - id
    t42 - id
    t43 - id
    t44 - id
    t45 - id
    t46 - id
    t47 - id
    t48 - id
    t49 - id
    t50 - id
    t51 - id

    g1 - id
    g2 - id
    g3 - id
    g4 - id
    g5 - id
    g6 - id
    g7 - id
    g8 - id
    g9 - id
"""

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
    msg = socket.recv()
    print("Received request: %s" % msg)
    # socket.send(b"Received")
    #  Send reply back to client
    socket.send(b"Received")
    return msg

def socket_predicates_exchange ():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    predicates = socket.recv()
    print("Received request: %s" % predicates)
    # socket.send(b"Received")
    #  Send reply back to client
    socket.send(b"Received")
    return predicates

