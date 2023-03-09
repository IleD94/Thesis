
from threading import Thread, Lock
import qi
import argparse
import sys
import time
import mydatabase





class SensorsThread (Thread):

    flag=True
    def __init__(self, arg_session, lock, kill_event):
        Thread.__init__(self)
        #Memory
        self.memory = arg_session.service("ALMemory")
        
        #Face detection
        self.face_detection = arg_session.service("ALFaceDetection")
        #pensare se aggiungere anche il microfono o meno, vedere piu avanti per capire come funziona
        #forse aggiungere anche il movimento tipo delle braccia

        # MOTION
        self.motion = arg_session.service("ALMotion")

        #autonomous life
        self.al=arg_session.service ("ALAutonomousLife")

        #queue
        self.lock = lock  # Get queue

        #round
        self.round = 0
    
        #kill event
        self.kill_event = kill_event

        #flag problem pddl created 
        self.flag = False

        #database functions
        self.mydatabase=mydatabase

        self.stablepred = []
        self.predicates = []
        self.predicates_to_check=[]
        self.myobj1=[]

    def create_predicates (self, people):
            mypredicates=['isAt',"Know", "Willing", "NotWilling", "Desire", "disjuncted_a", "isEmpathic"] #aggiungere isIn se si fa il riconoscimento degli oggetti
        #if self.round < 2 :
            predicates= []
            stablepred= []
            predicates_to_check = [] 
            myobj1=[]
            o=1
            i=3
            j=1
            k=5
            n=1
            stablepred = ["(isAt t1 robot room)\n","(isEnd end)\n","(isTrue t1)\n","(isTrue t2)\n","(isTrue t3)\n","(isTrue t4)\n","(isTrue t5)\n","(isTrue t6)\n",
                        "(isTrue t7)\n","(isTrue t8)\n","(isTrue t9)\n","(isTrue t10)\n","(isTrue t11)\n","(isTrue t12)\n","(isTrue t13)\n","(isTrue t14)\n",
                        "(isTrue t15)\n","(isTrue t16)\n","(isTrue t17)\n","(isTrue t18)\n","(isTrue t19)\n","(isTrue t20)\n","(isTrue t21)\n","(isTrue t22)\n",
                        "(taken t1)\n","(taken t2)\n","(taken t3)\n","(taken t4)\n","(taken t5)\n","(taken t6)\n",
                        "(taken t7)\n","(taken t8)\n","(taken t9)\n","(taken t10)\n","(taken t11)\n","(taken t12)\n","(taken t13)\n","(taken t14)\n",
                        "(taken t15)\n","(taken t16)\n","(taken t17)\n","(taken t18)\n","(taken t19)\n","(taken t20)\n","(taken t21)\n","(taken t22)\n",
                        "(free1 t23)\n","(free1 t24)\n","(free2 t25 t26)\n","(free2 t27 t28)\n","(free2 t49 t50)\n","(free3 t29 t30 t31)\n",
                        "(free3 t32 t33 t34)\n", "(free3 t35 t36 t37)\n", "(free3 t38 t39 t40)\n", "(free4 t41 t42 t43 t44)\n", "(free4 t45 t46 t47 t48)\n",
                        "(disjuncted_r room elsewhere)\n","(disjuncted_r elsewhere room)\n","(disjuncted ball box1)\n","(disjuncted box1 ball)\n","(disjuncted ball box2)\n",
                        "(disjuncted box2 ball)\n","(disjuncted emptySpace ball)\n","(disjuncted ball emptySpace)\n","(disjuncted box2 box1)\n","(disjuncted box1 box2)\n",
                        "(disjuncted box1 emptySpace)\n","(disjuncted emptySpace box1)\n","(disjuncted box2 emptySpace)\n","(disjuncted emptySpace box2)\n",
                        "(isIn t8 ball emptySpace)\n", "(isIn g1 ball box1)\n", "(isIn g3 ball box1)\n", "(isIn g4 ball box2)\n",
                        "(isIn g5 ball emptySpace)\n", ] 
            #print (mypredicates)
            for predicate in mypredicates:
                
                for person in people:
                    if person != "":
                        if predicate == "isAt":
                            o=o+1
                            predicates.append  ("("+ predicate +" t"+(str(o))+" "+ person + " room)\n")    
                        
                        if predicate == "isEmpathic": # si possono mettere anche altri stati mentali
                            predicates.append  ("("+ predicate +" "+ person + ")\n") 

                if len (people)>1:
                    if predicate == "Know":
                        i=i+1
                        j=j+1
                        stablepred.append  ("("+ predicate +" t"+(str(i))+ " "+ people[0] + " t"+(str(j))+")\n")
                        stablepred.append  ("("+ predicate +" t"+(str(i+1))+ " "+ people[0] + " t"+(str(j+1))+")\n")
                        k=k+1
                        n=n+1
                        stablepred.append  ("("+ predicate +" t"+(str(k))+ " "+ people[1] + " t"+(str(n))+")\n")
                        stablepred.append  ("("+ predicate +" t"+(str(k+1))+ " "+ people[1] + " t"+(str(n+1))+")\n")
                        stablepred.append  ("("+ predicate +" t9 " + people[0] + " t8)\n")
                        stablepred.append  ("("+ predicate +" t10 " + people[1] + " t8)\n")
                        #stablepred.append  ("("+ predicate +" t23 " + people[0] + " t16)\n")
                    
                    if predicate == "Willing":
                        stablepred.append  ("("+ predicate +" t14 " + people[0] + " g3)\n")
                        stablepred.append  ("("+ predicate +" t18 " + people[0] + " g5)\n")
                        stablepred.append  ("("+ predicate +" t22 " + people[0] + " g9)\n")
                        stablepred.append  ("("+ predicate +" t15 " + people[1] + " g4)\n")
                        stablepred.append  ("("+ predicate +" t13 " + people[1] + " g3)\n")
                        stablepred.append  ("("+ predicate +" t17 " + people[1] + " g5)\n")
                        stablepred.append  ("("+ predicate +" t19 " + people[1] + " g6)\n")
                        
                    
                    if predicate == "NotWilling":
                        stablepred.append  ("("+ predicate +" t16 " + people[0] + " g4)\n")
                        stablepred.append  ("("+ predicate +" t20 " + people[0] + " g7)\n")
                        stablepred.append  ("("+ predicate +" t21 " + people[1] + " g8)\n")

                    if predicate == "Desire":
                        stablepred.append  ("("+ predicate +" t11 " + people[1] + " g1)\n")
                        stablepred.append  ("("+ predicate +" t12 " + people[0] + " g2)\n")
                    
                    if predicate == "isAt":
                        stablepred.append  ("("+ predicate +" g7 " + people[0] + " elsewhere)\n")
                        stablepred.append  ("("+ predicate +" g9 " + people[0] + " room)\n")
                        stablepred.append  ("("+ predicate +" g6 " + people[1] + " elsewhere)\n")
                        stablepred.append  ("("+ predicate +" g2 " + people[1] + " elsewhere)\n")
                        stablepred.append  ("("+ predicate +" g8 " + people[1] + " room)\n")
                        

                    if predicate == "disjuncted_a":
                        stablepred.append  ("("+ predicate +" "+ people[0]+" "+ people[1]+")\n")
                        stablepred.append  ("("+ predicate +" "+ people[1]+" "+ people[0]+")\n")
                        stablepred.append ("("+ predicate +" "+ people[1]+" robot)\n")
                        stablepred.append ("("+ predicate +" "+ people[0]+" robot)\n")
                        stablepred.append  ("("+ predicate +" robot "+ people[1]+")\n")
                        stablepred.append  ("("+ predicate +" robot "+ people[0]+")\n")


            
            predicates_to_check=predicates
            print (predicates_to_check)
            new = predicates + stablepred
            indentation = "        "
            predicates = [indentation + x for x in new]
            "\n".join(predicates)
           #myobj1=[]
            for person in people:
                print (person)
                myobj1.append("    " + person + " - agent")
            myobj1.append("    robot - agent")
            myobj1='\n'.join(myobj1)


            # predicates_to_check = [] 
            # for predicate in mypredicates:
            #     for person in people:
            #         if person != "":
            #             if predicate == "isAt":
            #                 predicates.append  ("("+ predicate +" "+ person + " room)\n")

        #print (predicates)
        #self.flag = True
            return predicates_to_check, stablepred, predicates, myobj1

    #This fnction get face recognition from the sensor
    def face_rec(self):
        people= []
        counter = []
        my_people = []
        predicates = []
        myflag = True
        #reader_flag=False
        # tts1.setRecognitionEnabled(True)
        # time.sleep (0.2)
        #print (self.face_detection.isTrackingEnabled()) 
        if self.face_detection.isTrackingEnabled(): #risolvere il problema della testa            
            self.face_detection.setTrackingEnabled(False)
            time.sleep (10)

        if not self.face_detection.isRecognitionEnabled():
            self.face_detection.setRecognitionEnabled(True)
        
        myfriends= self.face_detection.getLearnedFacesList()
        #print (myfriends)

        #FORSE SERVE UN WHILE O UNA SOTTOSCRIZIONE CON CALLBACK QUA, COSi si possono fare i predicati?
        counter = [0,0,0,0]
        myfriends=['Ilenia', 'Federico', 'Giovanni', 'Serena']
        #self.queue.put("Not-Updated")
        flag  = True
        while flag:
            time.sleep (0.1)  
            face_detection_data=self.memory.getData("FaceDetected")
            my_people=[] ##########capire perche non funziona nell'altro modo, forse e una questione di tempo?
            #while myflag:
            #face_detection_data=self.memory.getData("FaceDetected")
            if len(face_detection_data)>1:
                faceInfoArray=face_detection_data[1]
                for i in range(len(faceInfoArray)-1):
                    faceID=faceInfoArray[i]
                    faceName=faceID[1]
                    my_people.append(faceName[2])
                #print (my_people)
            for i in range (len (myfriends)):
                if myfriends[i] in my_people:
                    counter [i]=counter[i]+1
                    #print (counter)
                if (counter[i]>4):
                    #print (counter[i])
                    people.append (myfriends[i])
                    k=i
                    for j in range (len (myfriends)):
                        if j==k:
                            continue
                        else:
                             if (counter[j] in range (2,4)):
                                 people.append (myfriends [j])

                    flag=False
            #print (counter)


        print ("THIS" + str(people))
        mynumber = len(my_people)
        #print (mynumber)
        self.predicates_to_check, self.stablepred, self.predicates, self.myobj1=self.create_predicates(people)
        self.lock.acquire()
        self.mydatabase.add_to_database(self.predicates,self.predicates_to_check,self.stablepred)
        self.lock.release()
        
        #queue.put(my_people)
        #print (people)
        #print ("########################################################################################")
        #flag = False

    def set_autonomous_abilities(self, blinking, background, awareness, listening, speaking):
        self.al.setAutonomousAbilityEnabled("AutonomousBlinking", blinking)
        self.al.setAutonomousAbilityEnabled("BackgroundMovement", background)
        self.al.setAutonomousAbilityEnabled("BasicAwareness", awareness)
        self.al.setAutonomousAbilityEnabled("ListeningMovement", listening)
        self.al.setAutonomousAbilityEnabled("SpeakingMovement", speaking)
        
    def run(self):
        #print("Boolean value in run:", self.running)
        print ("Thread '" + self.name + "' avviato")
        self.motion.setStiffnesses("Head", 1.0)
        self.motion.setAngles("Head", [0.0, 0.0], 0.1)
        while not self.kill_event.is_set():
            if self.flag == True:   
                self.round=+1
            self.set_autonomous_abilities (False, False, False, False, False)
            self.face_rec()
            #time.sleep (1)
        print ("Thread '" + self.name + "' terminato")
        exit(0)