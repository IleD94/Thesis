# coding=utf-8
import qi
import argparse
import sys
import requests
import time
import random
import zmq
# import threading
from collections import OrderedDict
from threading import Thread
from Queue import Queue


queue=Queue()
queue1=Queue()
running=True
flag=True
reader_flag=False
mypredicates=["isIn","notSame"]

def write_pddl (predicates, people, goal):
    # Define problem  PUò ESSERE UNA FUNZIONE, O (UNA CLASSE) RENDERLA IL PIù PERSONALIZZABILE POSSIBILE!
    prob1 = "(define \n    (problem simple_prob)\n    (:domain"
    test_dom="simple_dom"
    mydom =  " "+ test_dom +") \n "
    prob2 = "   (:objects \n        box - place\n        ball - objecto\n        room - place\n"
    myobj1=[]
    # while queue.empty():
    #     time.sleep(0.1)
    #people=queue.get()
    for person in people:
        myobj1.append("        " + person + " - person")
    l='\n'.join(myobj1)
    #ricordarsi di aggiungere anche gli altri oggetti, magari da sensore con i marker. Vedere come fare ##########################
    prob3 = "    \n)\n    (:init\n"
    #predicates = queue1.get()
    m=''.join([str(predicate) for predicate in predicates])
    myin = ("        "+ "\n    )\n"  )    
    #myinit=myin.replace()
    print("This is myin:")
    print (myin)
    prob4 = "    (:goal (and\n"

    mygoal= "        ("+str(goal)+  ")"  
            
    prob5= "\n    )  \n)    \n)"

    problem = prob1+mydom+prob2+l+prob3+m+myin+prob4+mygoal+prob5
    #print (problem) 
    # Write PDDL files    
    with open("problemio.pddl", "w") as f:
        f.write(problem)
    #flag = True


def ask_and_listen (string1):
    tts.say(string1)
    tts4.subscribe("WordRecognized")
    time.sleep(5)
    answ=tts2.getData("WordRecognized")
    #print(answ)
    tts4.unsubscribe("WordRecognized")
    return(answ)


def create_predicate (mypredicates, people):
    global flag
    predicates = []
    for predicate in mypredicates:
        for person in people:
            if person != "":
                if predicate == "isIn":
                    predicates.append  ("("+ predicate +" "+ person + " room)\n")
        if predicate == "notSame":
            predicates.append  ("("+ predicate +" "+ people[0]+" "+ people[1]+")\n")
            predicates.append  ("("+ predicate +" "+ people[1]+" "+ people[0]+")\n")
    stablepred = ["(isIn ball room)\n","(notSame room box)\n"]  
    predicates += stablepred
    indentation = "        "
    predicates = [indentation + x for x in predicates]
    "\n".join(predicates)
    queue1.put(predicates)
    
    flag = False
    print (predicates) 
    

class IlMioThread (Thread):
   def __init__(self, nome):
      Thread.__init__(self)
      self.nome = nome
   def run(self):
      #print("Boolean value in run:", self.running)
      print ("Thread '" + self.name + "' avviato")
      while(running):
        face_rec()
        #time.sleep (1)
      print ("Thread '" + self.name + "' terminato")
      exit(0)


def face_rec() :
    global people, tts2, predicates, flag, reader_flag
    counter=0
    predicates = []
    op = True
    #reader_flag=False
    tts2=session.service("ALMemory")
    tts1 = session.service("ALFaceDetection")
    # tts1.setRecognitionEnabled(True)
    # time.sleep (0.2)
    tts1.isRecognitionEnabled()
    a=tts1.isTrackingEnabled()  
    tts1.setRecognitionEnabled(True)
    time.sleep (0.2)  
    o=tts2.getData("FaceDetected")
    #people=[]
    while op:
        my_people = []
        my_people2 = []
        if len(o)>1:
            faceInfoArray=o[1]
            for i in range(len(faceInfoArray)-1):
                faceID=faceInfoArray[i]
                faceName=faceID[1]
                my_people.append(faceName[2])
            print (my_people)
            tts1.setRecognitionEnabled(False)
            time.sleep(0.2)
            print (my_people)
            #time.sleep (0.2)
        tts1.setRecognitionEnabled(True)
        time.sleep (0.2)
        o=tts2.getData("FaceDetected")
        if len(o)>1:
            faceInfoArray=o[1]
            for i in range(len(faceInfoArray)-1):
                faceID=faceInfoArray[i]
                faceName=faceID[1]
                my_people2.append (faceName[2])
            print (my_people2) 
            tts1.setRecognitionEnabled(False)   
            if my_people2 == my_people and '' not in my_people:
                counter = counter + 1
                print (counter)
        if counter > 7 :
            op = False
            people = my_people
            print ("this is my people:")
            print (people)
            queue.put(people)
    create_predicate (mypredicates, people)
    predicates=queue1.get()
    #reader_flag=True
    #print (reader_flag)
    print ("THIS" +str(people))
    w = tts1.isRecognitionEnabled()
    mynumber=len(people)
    print (mynumber)
    #queue.put(people)
    #print (people)
    print ("########################################################################################")
            


class StateMachine:

    def state_zero (self):
        # state zero: connection to pepper and its services, learning phase of faces
        global session, url,tts, tts2,tts4,socket
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")

        url='http://127.0.0.1:5000/'
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="130.251.13.191",
                            help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")
        args = parser.parse_args()
        
        session = qi.Session()
        try:
            session.connect("tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n")
            print("Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        tts = session.service("ALTextToSpeech")
        tts2=session.service("ALMemory")
        tts1=session.service
        thread1=IlMioThread("face_recognition")
        thread1.start()
        tts3 = session.service("ALSoundDetection")
        tts4=session.service("ALSpeechRecognition")
        tts4.setVocabulary(["no", "yes", "bob", "federico"],True)
        tts1 = session.service("ALFaceDetection")
        # ok= tts1.learnFace("Ilenia")
        # print(ok)
        tts4.setAudioExpression(True)
        time.sleep(3)
        self.current_state="state_one"

    
    def state_one(self):
        # state one: creation of domain and problem, call of the planner and creation of the plan
        global my_plan, flag, goal,mypredicates
        goal = socket.recv()
        print("Received request: %s" % goal)
        # socket.send(b"Received")
        #  Send reply back to client
        socket.send(b"Received")
        while flag:
            time.sleep(0.1)
            print ("SONO QUAAAAAAAAAAAAAAAAA")
        # while queue.empty():
        #     time.sleep(0.1)
        # while not reader_flag:
        #     time.sleep(0.1)
        people = queue.get()
            #reader_flag=False
        create_predicate (mypredicates, people)
        # while queue1.empty():
        #     time.sleep(0.1)
        predicates = queue1.get ()
        print (predicates)
        write_pddl(predicates,people,goal)
        mydir = "C:\Users\Lemonsucco\Desktop\Pepper\\"
        domain_path = mydir+'domain_simple.pddl'
        my_domain_list=[]
        with open (domain_path, "r") as f:
            for line in f:
                my_domain_list.append(line.strip())
        problem_path = mydir+'problemio.pddl'
        my_problem_list=[]
        with open (problem_path, "r") as f:
            for line in f:
                my_problem_list.append(line.strip())
        dict = {
            'domain': my_domain_list,
            'problem': my_problem_list
        }
        headers= {'Content-Type':'application/json'}
        response_put= requests.put(url+'planner_launch', json=dict, headers=headers)

        my_plan = response_put.text
        self.current_state = "state_two"
        
    def state_two(self):
        # state two: reading of the plan and its sequentialization
        global actions, n_action, my_plan_splitted
        actions = OrderedDict  ([
        ('action1' , 'ask_go_out'),
        ('action2' , 'ask_move_obj'),
        ('action3' , 'ask_call_someone'),
        ('action4' , 'ask_someone_obj_place'),
        ('action5' , 'laugh')
        ])
        
        myplan2 = my_plan.replace("'", " ")
        my_plan_3 = myplan2.replace('(', ' ')
        my_plan_last = my_plan_3.replace(')', ' ')

        my_plan_splitted = my_plan_last.split(' , ')
        n_action=len(my_plan_splitted)
        self.current_state = "state_three"
            
    def state_three(self):
        # state three: execution of actions and monitoring
        i=0
        for action in actions:
            print(action)
            u=my_plan_splitted[i].split()
            if i==0 or (i==n_action-1):
                a=u[1]
            else:
                a=u[0]
            tts.setLanguage('English')
            #print (a)
            #print (actions.get(action))
            #print (actions.values())
            if a in actions.values() :
                print(a)
                if a == actions.get('action1'):
                    # while queue.empty():
                    #     time.sleep(0.1)
                    # while not reader_flag:
                    #     time.sleep(0.1)
                    people = queue.get()
                        #reader_flag=False
                    #people = queue.get_nowait()
                    mynumber=len(people)
                    print (mynumber)
                    # while queue1.empty():
                    #     time.sleep(0.1)
                    predicates = queue1.get()
                    # print (predicates)
                    if len(people)>0: ########################### QUESTA ROBA NON STA FUNZIONANDO. CONTROLLARE PEOPLE, controllato è ok la dimensione
                        global myperson1
                        print ("ctyvghbunijmk")
                        mypredicates=["isIn","notSame"]
                        myperson1 = random.choice (people)
                        print ("Questa è myperson1:" + myperson1)
                        tts.say("Hello,I am Pepper!"+ myperson1 + "could you go out,please?")              
                        # print(people)
                        # print (myperson1)
                        # print(thatperson)
                        time.sleep(4)#
                        # while queue.empty():
                        #     time.sleep(0.1)
                        # while not reader_flag:
                        #     time.sleep(0.1)
                        people = queue.get()
                            #reader_flag=False
                        if myperson1 in people: ############################################################################Il problema potrebbe essere qua verificare domani
                            #.send(b"Received")
                            mypredicates=["isIn","notSame"]
                            print ("-----------------------------------TORNO AL PUNTO 1--------------------------------")
                            self.current_state = "state_one"
                            break    
                        mypredicates=["isIn","notSame"]
                        create_predicate(mypredicates,people)
                        # while queue1.empty():
                        #     time.sleep(0.1)
                        predicates=queue1.get()
                if a == actions.get('action2'):
                    print ('sto qua')
                    print (a)
                    # while queue.empty():
                    #     time.sleep(0.1)
                    # while reader_flag:
                    #     time.sleep(0.1)
                    # people = queue.get()
                        #reader_flag=False
                    print (len(people))
                    while (len(people)<1)or(len(people)>1):
                        print ("########")
                        print (people)
                        print("Sto loop de merda ##############")
                        time.sleep(0.1)
                        # while queue.empty():
                        #     time.sleep(0.1)
                        # while not reader_flag:
                        #     time.sleep(0.1)
                        # people = queue.get()
                            #reader_flag=False
                        mypredicates=["isIn","notSame"]
                        create_predicate(mypredicates,people)
                        # while queue1.empty():
                        #     time.sleep(0.1)
                        predicates=queue1.get()
                    print (people[0])
                    mypersona = people[0]
                    mypredicates=["isIn","notSame"]
                    create_predicate(mypredicates,people)
                    predicates=queue1.get()
                    tts.say(mypersona+"could you move the ball into the box,please?")
                    time.sleep(3)
                    mypredicates=["isIn","notSame"]
                    create_predicate(mypredicates,people)
                    # while queue1.empty():
                    #     time.sleep(0.1)
                    predicates=queue1.get()
                    answ = ask_and_listen(mypersona+"have you put the ball into the box?")
                    counter=0
                    while ("no" in str(answ)):
                        counter = counter+1
                        answ = ask_and_listen(mypersona+"have you put the ball into the box?")
                        if counter == 3 :
                            self.current_state = "state_one"
                            break
                if a == actions.get('action3'):
                    # while queue.empty():
                    #     time.sleep(0.1)
                    # while not reader_flag:
                    #     time.sleep(0.1)
                    # people = queue.get()
                        #reader_flag=False
                    while (len(people)<1)or(len(people)>1):
                        # while queue.empty():
                        #     time.sleep(0.1)
                        # while not reader_flag:
                        #     time.sleep(0.1)

                        #people = queue.get()
                            #reader_flag=False
                        print ("########")
                        print (people)
                        print("Sto loop de merda ##############")
                        time.sleep(0.1)
                        mypredicates=["isIn","notSame"]
                        create_predicate(mypredicates,people)
                        # while queue1.empty():
                        #     time.sleep(0.1)
                        predicates=queue1.get()
                    mypersone = people[0] ###########################non sta funzionando, capire il perche
                    # print (people)
                    # print (mypersone) #############problema con questo nome, risolvere con piu persone per esperimento
                    mypredicates=["isIn","notSame"]
                    create_predicate(mypredicates,people)
                    # while queue1.empty():
                    #     time.sleep(0.1)
                    predicates=queue1.get()
                    answ = ask_and_listen (mypersone+"Could you call"+ myperson1+ "back, please?")
                    counter=0
                    while not ("yes" in str(answ)): #################si puo mettere anche si o no
                        answ = ask_and_listen(mypersone+"have you called"+ myperson1 +" ?")
                        counter = counter + 1
                        if counter == 3:
                            self.current_state=="state_one"
                            break
                if a == actions.get('action4'):
                    # while queue.empty():
                    #     time.sleep(0.1)
                    # while not reader_flag:
                    #     time.sleep(0.1)
                    # people = queue.get()
                        #reader_flag=False
                    time.sleep(3)
                    print (myperson1)
                    mypredicates=["isIn","notSame"]
                    create_predicate(mypredicates,people)
                    # while queue1.empty():
                    #     time.sleep(0.1)
                    predicates=queue1.get()
                    counter=0
                    while not (myperson1 in people):
                        #print(people)
                        counter = counter+1
                        print ("-----------------------------------NON TROVO MYPERSON1--------------------------------")
                        time.sleep(1)
                        # while queue.empty():
                        #     time.sleep(0.1)
                        # while not reader_flag:
                        #     time.sleep(0.1)
                        # people = queue.get()
                            #reader_flag=False
                        mypredicates=["isIn","notSame"]
                        create_predicate(mypredicates,people)
                        # while queue1.empty():
                        #     time.sleep(0.1)
                        predicates=queue1.get()
                        if counter == 20:
                            self.current_state = "state_one"
                            break
                    answ = ask_and_listen("Hi, "+ myperson1 + "Do you know where the ball is?")
                    if ("yes" in str(answ)):
                        #socket.send(b"Received")
                        mypredicates=["isIn","notSame"]
                        create_predicate(mypredicates,people)
                        # while queue1.empty():
                        #     time.sleep(0.1)
                        predicates=queue1.get()
                        self.current_state="state_one"
                        break
                    else:
                        answ = ask_and_listen("are you sad?")  
                        if ("no" in str(answ)):
                            #socket.send(b"Received")
                            mypredicates=["isIn","notSame"]
                            create_predicate(mypredicates,people)
                            # while queue1.empty():
                            #     time.sleep(0.1)
                            predicates=queue1.get()
                            self.current_state="state_one"
                            break
                        else:
                            mypredicates=["isIn","notSame","isSad"]
                            create_predicate(mypredicates,people)
                            # while queue1.empty():
                            #     time.sleep(0.1)
                            predicates=queue1.get()
                if a == actions.get('action5'):
                    global running
                    mypredicates=["isIn","notSame", "isSad", "isHappy"]
                    create_predicate(mypredicates,people)
                    # while queue1.empty():
                    #     time.sleep(0.1)
                    predicates=queue1.get()
                    if "isSad"+ myperson1 in predicates:
                        tts.say ("I'm happy!! I've reached my goal")
                        running = False
                        time.sleep(1)
                        exit(0)
                    else:
                        self.current_state = "state_one"
                        break

            ########################### SE IL MONITORAGGIO DA ESITO NEGATIVO METTERE UN BREAK, COSi TORNA ALLO STATO ONE
            ##else:
                ##break
            if i< n_action-1:
                i=i+1
        self.current_state = "state_one" #  HERE WE REPLAN OUR PLANNER BECAUSE THE ACTION IS NOT IN THE LIST