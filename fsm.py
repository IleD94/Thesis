import qi
import argparse
import sys
import requests
import time
from collections import OrderedDict
from threading import Thread

class IlMioThread (Thread):
   def __init__(self, nome, durata):
      Thread.__init__(self)
      self.nome = nome
      self.durata = durata
   def run(self):
      print ("Thread '" + self.name + "' avviato")
      face_rec()
      print ("Thread '" + self.name + "' terminato")

def face_rec() :
    

class StateMachine:

    def state_zero (self):
        # state zero: connection to pepper and its services, learning phase of faces
        global session, url,tts, tts2,tts1,tts4
        url='http://127.0.0.1:5000/'
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="130.251.13.102",
                            help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")
        
        #parser.add_argument(sys.argv[1])

        #parser.add_argument(sys.argv[2])
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
        self.current_state="state_one"
        tts1 = session.service("ALFaceDetection")
        tts3 = session.service("ALSoundDetection")
        tts1.setRecognitionEnabled(True)
        tts1.isRecognitionEnabled()
        a=tts1.isTrackingEnabled()
        tts1.learnFace("Federico")
        tts4=session.service("ALSpeechRecognition")
        #tts4.removeAllContext()
        tts4.setVocabulary(["no", "yes", "bob", "federico"],True)
        #tts4.subscribe("test_ASR")
        #time.sleep(5)
        #tts4.unsubscribe("test_ASR")
        
        tts4.setAudioExpression(True)
        time.sleep(3)
        o=tts2.getData("FaceDetected")
        #o=tts1.subscribe("Test_Face")
        #print (o[1])
        #tts1.forgetPerson("Ilenia")
        lista=tts1.getLearnedFacesList()
        print (lista)
        #print (o)
        #a = FaceDetected()
        #print (a)
        time.sleep(4)


    
    def state_one(self):
        # state one: creation of domain and problem, call of the planner and creation of the plan
        global my_plan
        #url='http://127.0.0.1:5000/'
        mydir = "C:\Users\Lemonsucco\Desktop\Pepper\\"
        domain_path = mydir+'domain_simple.pddl'
        my_domain_list=[]
        with open (domain_path, "r") as f:
            for line in f:
                my_domain_list.append(line.strip())
        problem_path = mydir+'problem_simple.pddl'
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
        #print(response_put.status_code)
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
        #print(my_plan_last)
        #print (n_action)
        self.current_state = "state_three"
            
    def state_three(self):
        # state three: execution of actions and monitoring(il monitoraggio non fa parte delle azioni che arrivano dal planner, crearlo in base all'azione)
        i=0
        people = []
        o=tts2.getData("FaceDetected",0)
        if len(o)>1:
            faceInfoArray=o[1]
            for i in range(len(faceInfoArray)-1):
                faceID=faceInfoArray[i]
                faceName=faceID[1]
                people.append(faceName[2])
            #tts1.setRecognitionEnabled(False)
            w = tts1.isRecognitionEnabled()
            print (w)
            print (people)
            print (len(people))
        #time.sleep(5)
        for action in actions:
        # print (actions.get(action))
            #print (my_plan_splitted[i])
            #print (len(my_plan_splitted))
            u=my_plan_splitted[i].split()
            if i==0 or (i==n_action-1):
                a=u[1]
            else:
                a=u[0]
            #print (u)
            tts.setLanguage('English')
            if a in str(actions.get(action)) :
                #tt3=session.service("ALAnimatedSpeech")
                configuration = {"bodyLanguageMode":"contextual"}
                if a == actions.get('action1'):
                    if len(people)>0:
                        global myperson1
                        thatperson = people
                        myperson1 = str(people)
                        tts.say("Hello,I am Pepper!"+ myperson1 + "could you go out,please?")              
                        # w=tts1.setRecognitionEnabled(True)
                        # print (w)
                        print(people)
                        print (myperson1)
                        print("QUI")
                        print(thatperson)
                        if any(item in thatperson for item in people):
                            self.current_state = "state_one"
                            break    
                if a == actions.get('action2'):
                    while not (len(people)>0):
                        print (people)
                        time.sleep(1)
                    myperson= str(people)
                    tts.say(myperson+"could you move the ball into the box,please?")
                    time.sleep(6)
                    tts.say(myperson+"have you put the ball into the box?")
                    tts4.subscribe("WordRecognized")
                    time.sleep(5)
                    answ=tts2.getData("WordRecognized")
                    print(answ)
                    tts4.unsubscribe("WordRecognized")
                    #tts4.removeAllContext()
                    while ("no" in str(answ)):
                        tts.say(myperson+"have you put the ball into the box?")
                        tts4.setLanguage('English')
                        tts4.subscribe("WordRecognized")
                        time.sleep(5)
                        answ=tts2.getData("WordRecognized")
                        print(answ)
                        tts4.unsubscribe("WordRecognized")
                        #tts4.removeAllContext()
                
                if a == actions.get('action3'):
                    myperson= str(people)
                    print (people)
                    print (myperson) #############problema con questo nome, risolvere con piu persone per esperimento
                    tts.say(myperson+"Could you call"+ myperson1+ "back, please?")
                    time.sleep(4)
                    tts4.subscribe("WordRecognized")
                    time.sleep(5)
                    answ=tts2.getData("WordRecognized")
                    print(answ)
                    tts4.unsubscribe("WordRecognized")
                    #tts4.removeAllContext()
                    while not ("yes" in str(answ)): #################si puo mettere anche si o no
                        tts4.setLanguage('Italian')
                        tts.say(myperson+"have you called federico?")
                        tts4.subscribe("WordRecognized")
                        time.sleep(5)
                        answ=tts2.getData("WordRecognized")
                        print (answ)
                        tts4.unsubscribe("WordRecognized")
                if a == actions.get('action4'):
                    time.sleep(4)
                    print (myperson1)
                    while not (myperson1 in str(people)):
                        print(people)
                        time.sleep(1)
                    tts.say ("Hi "+ myperson1+ "Do you know where is the ball?")
                    tts4.subscribe("WordRecognized")
                    time.sleep(5)
                    answ=tts2.getData("WordRecognized")
                    print (answ)
                    tts4.unsubscribe("WordRecognized")
                    #tts4.removeAllContext()
                    if ("yes" in str(answ)):
                        self.current_state="state_one"
                        break
                    else:
                        tts.say("are you sad?")
                        tts4.subscribe("WordRecognized")
                        time.sleep(5)
                        answ=tts2.getData("WordRecognized")
                        print (answ)
                        tts4.unsubscribe("WordRecognized")
                        #tts4.removeAllContext()
                        if ("no" in str(answ)):
                            self.current_state="state_one"
                            break
                if a== a == actions.get('action5'):
                    tts.say ("I'm happy!! I reached my goal")
                    exit (0)

            ########################### SE IL MONITORAGGIO DA ESITO NEGATIVO METTERE UN BREAK, COSi TORNA ALLO STATO ONE
            else:
                break
            if i< n_action-1:
                i=i+1
        self.current_state = "state_one" #  HERE WE REPLAN OUR PLANNER BECAUSE THE ACTION IS NOT IN THE LIST