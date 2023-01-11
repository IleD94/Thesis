import qi
import argparse
import sys
import requests
import time
from collections import OrderedDict


class StateMachine:

    def state_zero (self):
        # state zero: connection to pepper and its services, learning phase of faces
        global session, url,tts, tts2
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
        tts1.isRecognitionEnabled()
        a=tts1.isTrackingEnabled()
        #print (a)
        time.sleep(5)
        #w=tts1.learnFace("Ilenia")
        #print (w)
        o=tts2.getData("FaceDetected")
        #o=tts1.subscribe("Test_Face")
        #print (o[1])
        #tts1.forgetPerson("Ilenia")
        lista=tts1.getLearnedFacesList()
        #print (lista)
        #print (o)
        #a = FaceDetected()
        #print (a)


    
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
        ('action5' , 'laugh'),
        #('action6' , 'know_isputting_infer_know_isin'),
        #('action7' , 'know_iamputting_infer_know_isin'),
        #('action8' , 'know_isgoing_infer_know'),
        #('action9' , 'know_isin_infer_know_isgoing'),
        #('action10' , 'know_isgoing_afterphase'),
        #('action11' , 'know_iamgoing_afterphase'),
        #('action12' , 'test')
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
            if a in str(actions) :
                n = my_plan.count(actions.get(action))
                #print (n)
                #time.sleep (4)
                tts.setLanguage('English')
                #tts.say(a)
                o=tts2.getData("FaceDetected",0)

                faceInfoArray=o[1]
                #print (faceInfoArray)
                # print (len(faceInfoArray))
                # faceID=faceInfoArray[0]
                # faceName=faceID[1]
                # print(faceName[2])
                # faceID=faceInfoArray[1]
                # faceName=faceID[1]
                # print(faceName[2])
                people = []
                for i in range(len(faceInfoArray)-1):
                    faceID=faceInfoArray[i]
                    faceName=faceID[1]
                    people.append(faceName[2])
                print (people)
                
            ########################### SE IL MONITORAGGIO DA ESITO NEGATIVO METTERE UN BREAK, COSi TORNA ALLO STATO ONE
            else:
                break
            if i< n_action-1:
                i=i+1
        self.current_state = "state_one" #  HERE WE REPLAN OUR PLANNER BECAUSE THE ACTION IS NOT IN THE LIST
