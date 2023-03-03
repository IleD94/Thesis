
from threading import Thread, Lock
import qi
import argparse
import sys
from Queue import Queue
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

        #database functions
        self.mydatabase=mydatabase

        self.stablepred = []
        self.predicates = []
        self.predicates_to_check=[]
        self.myobj1=[]

    def create_predicates (self, people):
        mypredicates=['isAt',"Know", "Willing", "NotSureIfWilling", "Ignore", "disjuncted_a"] #aggiungere isIn se si fa il riconoscimento degli oggetti
        if self.round < 2 :
            predicates= []
            stablepred= []
            predicates_to_check = [] 
            myobj1=[]
            o=1
            i=3
            j=1
            k=5
            n=1
            stablepred = ["(isAt t1 robot room)\n","(hasStartAgent robot)\n","(isEnd end)\n","(isStart t1)\n","(isStart t2)\n","(isStart t3)\n","(isStart t4)\n","(isStart t5)\n","(isStart t6)\n",
                        "(isStart t7)\n","(isStart t8)\n","(isStart t9)\n","(isStart t10)\n","(isStart t11)\n","(isStart t12)\n","(isStart t13)\n","(isStart t14)\n",
                        "(isStart t15)\n","(isStart t16)\n","(isStart t23)\n","(free t17)\n","(free t18)\n","(free t19)\n","(free t20)\n","(free t21)\n","(free t22)\n",
                        "(disjuncted_id t17 t18)\n","(disjuncted_id t17 t19)\n","(disjuncted_id t17 t20)\n","(disjuncted_id t17 t21)\n","(disjuncted_id t17 t22)\n",
                        "(disjuncted_id t18 t19)\n","(disjuncted_id t18 t20)\n","(disjuncted_id t18 t21)\n","(disjuncted_id t18 t22)\n","(disjuncted_id t19 t20)\n",
                        "(disjuncted_id t19 t21)\n","(disjuncted_id t19 t22)\n","(disjuncted_id t20 t21)\n","(disjuncted_id t20 t22)\n","(disjuncted_id t21 t22)\n",
                        "(disjuncted_r room elsewhere)\n","(disjuncted_r elsewhere room)\n","(disjuncted ball box1)\n","(disjuncted box1 ball)\n","(disjuncted ball box2)\n",
                        "(disjuncted box2 ball)\n","(disjuncted emptySpace ball)\n","(disjuncted ball emptySpace)\n","(disjuncted box2 box1)\n","(disjuncted box1 box2)\n",
                        "(disjuncted box1 emptySpace)\n","(disjuncted emptySpace box1)\n","(disjuncted box2 emptySpace)\n","(disjuncted emptySpace box2)\n","(disjuncted room box1)\n",
                        "(disjuncted box1 room)\n","(disjuncted room emptySpace)\n","(disjuncted emptySpace room)\n","(disjuncted box2 room)\n","(disjuncted room box2)\n", "(isIn t8 ball emptySpace)\n"] 

            for predicate in mypredicates:
                for person in people:
                    if person != "":
                        if predicate == "isAt":
                            o=o+1
                            predicates.append  ("("+ predicate +" t"+(str(o))+" "+ person + " room)\n")                   
                if len (people)>1:
                    if predicate == "Know":
                        i=i+1
                        j=j+1
                        stablepred.append  ("("+ predicate +" t"+(str(i))+ " "+ people[0] + " t"+(str(j))+")\n")
                        k=k+1
                        n=n+1
                        stablepred.append  ("("+ predicate +" t"+(str(k))+ " "+ people[1] + " t"+(str(n))+")\n")
                        stablepred.append  ("("+ predicate +" t9 " + people[0] + " t8)\n")
                        stablepred.append  ("("+ predicate +" t5 " + people[0] + " t3)\n")
                        stablepred.append  ("("+ predicate +" t7 " + people[1] + " t3)\n")
                        stablepred.append  ("("+ predicate +" t10 " + people[1] + " t8)\n")
                        #stablepred.append  ("("+ predicate +" t23 " + people[0] + " t16)\n")
                    
                    if predicate == "Willing":
                        stablepred.append  ("("+ predicate +" t11 " + people[0] + " t8)\n")
                        stablepred.append  ("("+ predicate +" t12 " + people[1] + " t8)\n")
                        stablepred.append  ("("+ predicate +" t13 " + people[0] + " t2)\n")
                    
                    if predicate == "NotSureIfWilling":
                        stablepred.append  ("("+ predicate +" t14 " + people[1] + " t3)\n")

                    if predicate == "Ignore":
                        stablepred.append  ("("+ predicate +" t15 " + people[1] + " t16)\n")
                        stablepred.append  ("("+ predicate +" t23 " + people[0] + " t16)\n")

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
            
            for person in people:
                myobj1.append("        " + person + " - agent")
            myobj1.append("        robot - agent")
            myobj1='\n'.join(myobj1)

        
        else:
            predicates_to_check = [] 
            for predicate in mypredicates:
                for person in people:
                    if person != "":
                        if predicate == "isAt":
                            predicates.append  ("("+ predicate +" "+ person + " room)\n")

        #print (predicates)
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
            self.round=+1
            self.set_autonomous_abilities (False, False, False, False, False)
            self.face_rec()
            #time.sleep (1)
        print ("Thread '" + self.name + "' terminato")
        exit(0)