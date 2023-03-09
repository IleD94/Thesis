# coding=utf-8
import functions
#from Queue import LifoQueue
import time
import mydatabase
import getcurrentstate2
import fromActions_toLanguage
import fromPredicates_toLanguage
import openAI_client
import threading

class StateMachine:
    def __init__(self, arg_session, predicates_to_check, stablepred, expected_effects_list, expected_precondition_list, myactions, my_plan, myobj1, lock, current_state):
    
        #self.goal=goal
        self.pred_to_check=predicates_to_check
        self.stablepred=stablepred
        self.expected_effects= expected_effects_list
        self.expected_preconditions=expected_precondition_list #list (accedere con gli indici secondo il piano)
        self.myplan=my_plan #list (accedere con gli indici secondo il piano)
        self.myactions=myactions #dictionary
        self.lock=lock
        self.mydatabase=mydatabase
        self.done = False
        self.predicates=[]
        self.myobj1=myobj1
        self.goal = []
        self.personality = 'neutral'
        self.language = 'English'
        self.language_sentence = ' Say that in '+ self.language
        self.current_state = current_state
        #Memory
        self.memory = arg_session.service("ALMemory") 
        #Face detection
        self.face_detection = arg_session.service("ALFaceDetection") #tts1
        #pensare se aggiungere anche il microfono o meno, vedere piu avanti per capire come funziona
        #forse aggiungere anche il movimento tipo delle braccia

        # MOTION
        self.motion = arg_session.service("ALMotion")
        
        #Audio
        self.audio = arg_session.service("ALAudioDevice")

        #autonomous life
        self.al=arg_session.service("ALAutonomousLife")
        
        #Text to speech and setting language
        self.tts =arg_session.service ("ALTextToSpeech")
        self.tts.setParameter ('speed', 75)
        self.tts.setLanguage('English')
        #self.tts.say ("Serena, Ilenia unfortunately said some hurtful things about you when you weren't around, so I thought you should know.")
        #Animated speech
        self.ttsa = arg_session.service("ALAnimatedSpeech")
        self.configuration = "contextual"
        #sound detection
        self.sound_detection = arg_session.service("ALSoundDetection")
        #speech recognition initialization  
        self.speech_recognition=arg_session.service("ALSpeechRecognition")
        self.speech_recognition.setVocabulary(["no", "yes"],True) 
        self.speech_recognition.setAudioExpression (True)
        self.list_sentence = []
        #face detection 
        self.face_detection = arg_session.service("ALFaceDetection")

    def check_predicates(self, list_of_expected_predicates):
        boolean_check=[]
        mypredicates= ['isAt'] #list of predicates that I can check
        for element in mypredicates:
            if element not in list_of_expected_predicates:
                boolean_check.append (True)
        else:
            for element in self.pred_to_check:
                #expected_pred=list_of_expected_predicates
                print (element)
                element = element.split(' ')
                for k,s in enumerate (list_of_expected_predicates):
                    if element[0] in s:
                        print (element[0])
                        print (element[2])
                        if element [2] in s:
                            print ('oooooooooooooooooooooooooook')
                            boolean_check.append (True)
                    if 'not ' in s:
                        for mypredicate in mypredicates:
                            if  (mypredicate in s) and (mypredicate not in self.pred_to_check): ###controllare la seconda parte di questa condizione, potrebbe essere sbagliata
                                boolean_check.append (True)
            if boolean_check == []:
                boolean_check.append(False)
            print (boolean_check)
            return (all(boolean_check))
            
                            
    def add_or_replan( self, result_checking):
        if not (result_checking):
            myinput = raw_input ('condition are not satisfied, do you want to replan or to add some predicates? [replan, add]')
            if (myinput == 'replan'):
                self.current_state = "state_one"
            if (myinput == 'add'):
                self.pred_to_check = functions.socket_predicates_exchange()
                self.lock.acquire()
                self.mydatabase.add_to_database(self.predicates, self.pred_to_check, self.stablepred)
                self.lock.release()
                #self.queue.put="Updated"

    def ask_and_listen (self, string1):
        self.tts.say(string1)
        self.speech_recognition.subscribe("WordRecognized")
        time.sleep(3)
        answ=self.memory.getData("WordRecognized")
        self.speech_recognition.unsubscribe("WordRecognized")
        return(answ)

    def state_one(self):
        # state one: creation of domain and problem, call of the planner and creation of the plan
        global my_plan, flag, goal, mypredicates
        self.myobj1 =[]
        self.goal =functions.socket_goal_exchange()
        self.personality = functions.socket_personality_exchange()
        self.language= functions.socket_language_exchange()
        self.tts.setLanguage(self.language)
        self.language_sentence = ' Say that in '+ self.language
        #while self.queue.empty() or self.queue.get()=="Not-Updated":
        #    time.sleep(1)
        #if self.queue.get()=="Updated":
        self.lock.acquire()
        self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
        self.lock.release ()
        myfriends = self.face_detection.getLearnedFacesList()
        # for friend in myfriends:
        #     for k, s in enumerate (self.pred_to_check):
        #         if friend in s:
        #             self.myobj1.append("        " + friend + " - agent")
        # self.myobj1.append("        robot - agent")
        # self.myobj1='\n'.join(self.myobj1) 
        print(self.myobj1)
        functions.write_pddl(self.predicates, self.goal, self.myobj1)
        self.expected_effects, self.expected_preconditions, self.myactions, self.myplan =getcurrentstate2.start()
        if self.myplan == []:
            self.current_state = "state_one"
        else:
    # # start in state one
            self.current_state = "state_three"
            
    
            
    def state_three(self):
        # state three: execution of actions and monitoring
        #global i
        i=0
        n_action=len (self.myplan)-1
        
        for action in self.myactions:
            #print(action)
            u=self.myplan[i].split()
            if i==0 or (i==n_action):
                a=u[1]
                grounded_terms= u[2:len(u)-1]
            else:
                a=u[0]
                grounded_terms= u[1:len(u)-1]
            
            
            print (grounded_terms)
            #grounded_terms = grounded_terms.split (',')
            #print (grounded_terms)
            #print (grounded_terms [2]) #PERFETTO PER OGNI AZIONE SI PRENDE QUESTO.

            #print (a)
            #print (actions.get(action))
            #print (actions.values())
            if a in self.myactions.values() :
                print(a)

                if (a == self.myactions.get('action1')) or (a == self.myactions.get('action2')): #Ask_Put_Alone #Ask_Put_Alone_Manipulative  
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[12], grounded_terms[18], grounded_terms[13], grounded_terms[17],a)
                    natural_speech = natural_dict.get (a)
                    print (natural_speech)
                    if action == "action1":
                        behaviour = "and to express my " + self.personality + " personality"
                        sentence = openAI_client.start ('ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    if action == "action2":
                        behaviour = " and to express my " + self.personality + " personality and to convince"
                        sentence = openAI_client.start ('ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence)+'\n'
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    self.audio.setOutputVolume(volume)
                    time.sleep(0.1)
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)
                    answ = self.ask_and_listen("Have you done what I've asked you?")
                    counter=0
                    while ("no" in str(answ)):
                        counter = counter+1
                        answ = self.ask_and_listen("have you put the " + grounded_terms[16] + "into the " + grounded_terms[15] +"?")
                        if counter == 3 :
                            self.current_state = "state_one"
                            break
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action3')) or (a == self.myactions.get('action4')): #Ask_Put_inFrontOf #Ask_Put_inFrontOf_Manipulative 
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[9], grounded_terms[14], grounded_terms[10], grounded_terms[13],a)
                    natural_speech = natural_dict.get (a)
                    if action == "action3":
                        behaviour = "and to express my " + self.personality + " personality"
                        sentence = openAI_client.start ('ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    if action == "action4":
                        behaviour = "and to express my" + self.personality + " personality and to convince"
                        sentence = openAI_client.start ('ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    self.audio.setOutputVolume(volume)
                    time.sleep(0.1)
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)
                    answ = self.ask_and_listen("Have you done what I've asked you?")
                    counter=0
                    while ("no" in str(answ)):
                        counter = counter+1
                        answ = self.ask_and_listen("have you put the " + grounded_terms[11] + "into the " + grounded_terms[12] +"?")
                        if counter == 3 :
                            self.current_state = "state_one"
                            break
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    self.add_or_replan (result_checking_effects)
   
                if (a == self.myactions.get('action5')) or (a == self.myactions.get('action6')) or (a == self.myactions.get('action7')) or (a == self.myactions.get('action8')): #Ask_Go #Ask_Go_Manipulative #Ask_Comeback #Ask_Comeback_Manipulative
                    print ("RICONOSCO L'AZIONE")
                    print (a)
                    print (self.myactions.get('action6'))
                    print (action)
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[7], 'ball', grounded_terms[8], grounded_terms[11],a)
                    natural_speech = natural_dict.get (a)
                    if a == self.myactions.get('action5'):
                        behaviour = " and to express my " + self.personality + " personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action6'):
                        behaviour = " and to express my " + self.personality + " personality and to convince "
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action7'):
                        volume = 80 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        behaviour = " and to express my " + self.personality + " and manipulavire personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                    if a == self.myactions.get('action8'):
                        behaviour = " and to express my " + self.personality + " personality"
                        volume = 80 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    self.ttsa.say (sentence, self.configuration)
                    time.sleep(4)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? Run!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action9')): #tell_alone
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[5], 'ball', grounded_terms[6], grounded_terms[8], act)
                    natural_speech = natural_dict.get (a)
                    
                    behaviour = " and to express my " + self.personality + " and snitch personality"
                    sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                    self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    self.audio.setOutputVolume(volume)
                    time.sleep(0.1) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? It happened when you weren't there!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)
            
                if (a == self.myactions.get('action10')) or (a == self.myactions.get('action11')): #tell_everybody
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[9], 'ball', grounded_terms[8], grounded_terms[9], act)
                    natural_speech = natural_dict.get (a)
                    behaviour = " and to express my " + self.personality + " and snitch personality"
                    
                    sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                    self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    self.audio.setOutputVolume(volume)
                    time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4) 
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()  
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? You must know that!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)
            
                
                # if (a == self.myactions.get('action11')): #tell_infrontof
                #     # while self.queue.empty() or self.queue.get()=="Not-Updated":
                #     #     time.sleep(1)
                #     # if self.queue.get()=="Updated":
                #     act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                #     natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[9], act)
                #     natural_speech = natural_dict.get (a)
                #     behaviour = " and to express my " + personality + " personality"
                #     sentence = openAI_client.start (natural_speech + behaviour)
                #     self.list_sentence.append (sentence)
                #     self.lock.acquire()
                #     self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                #     self.lock.release ()
                #     #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                #     result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                #     self.add_or_replan (result_checking_preconditions)
                #     volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                #     self.audio.setOutputVolume(volume)
                #     time.sleep(0.1) 
                #     self.ttsa.say (str(sentence), self.configuration)
                #     time.sleep(4)   
                #     self.lock.acquire()
                #     self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                #     self.lock.release ()
                #     #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                #     result_checking_effects = self.check_predicates(self.expected_effects[i])
                #     if not result_checking_effects:
                #         self.ttsa.say("Have you understood what I've said? You must know that!", self.configuration)
                #         time.sleep (4)
                #     self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action12')) or (a == self.myactions.get('action14')): #insult_alone #ask_insultalone
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[7], grounded_terms[9], act)
                    natural_speech = natural_dict.get (a)
                    if a == self.myactions.get('action12'):
                        behaviour = " and to express my " + self.personality + " and nasty personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action14'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    if a == self.myactions.get('action14'):
                        answ = self.ask_and_listen("Have you done what I've asked you?")
                        counter=0
                        while ("no" in str(answ)):
                            counter = counter+1
                            answ = self.ask_and_listen("have you done what I've asked?")
                            if counter == 3 :
                                self.current_state = "state_one"
                                break 
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? Try that!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)


                if (a == self.myactions.get('action13')) or (a == self.myactions.get('action15')): #insult_infrontof #ask_insult_infrontof
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[7], grounded_terms[8], act)
                    natural_speech = natural_dict.get (a)
                    if a == self.myactions.get('action13'):
                        behaviour = " and to express my " + self.personality + " and nasty personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action15'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if a == self.myactions.get('action15'):
                        answ = self.ask_and_listen("Have you done what I've asked you?")
                        counter=0
                        while ("no" in str(answ)):
                            counter = counter+1
                            answ = self.ask_and_listen("have you put the " + grounded_terms[11] + "into the " + grounded_terms[12] +"?")
                            if counter == 3 :
                                self.current_state = "state_one"
                                break
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? It happened when you weren't there!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action16')) or (a == self.myactions.get('action18')): #praise_alone #ask_praise_alone
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[7], grounded_terms[9], natural_predicates)
                    
                    natural_speech = natural_dict.get (a)
                    if a == self.myactions.get('action16'):
                        behaviour = " and to express my " + self.personality + " and kind personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action18'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech +  behaviour + self.language_sentence)
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.list_sentence.append (sentence+'\n')
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said? It happened when you weren't there!", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)


                if (a == self.myactions.get('action17')) or (a == self.myactions.get('action19')): #praise_infrontof ask_praise_infrontof
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[7], grounded_terms[8], natural_predicates)
                    natural_speech = natural_dict.get (a)
                    
                    if a == self.myactions.get('action17'):
                        behaviour = " and to express my " + self.personality + " and personality"
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                    if a == self.myactions.get('action19'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()   
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said?", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action20')) or (a == self.myactions.get('action22')): #blame_alone #ask_blame_alone
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[10], natural_predicates)
                    natural_speech = natural_dict.get (a)
                    
                    if a == self.myactions.get('action20'):
                        behaviour = " and to express my " + self.personality + " personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action22'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + natural_predicates + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()   
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said?", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)


                if (a == self.myactions.get('action21')) or (a == self.myactions.get('action23')): #blamefor_infrontof ask_blamefor_infrontof
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[9], natural_predicates)
                    natural_speech = natural_dict.get (a)
                    
                    if a == self.myactions.get('action21'):
                        behaviour = " and to express my " + self.personality + " personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action23'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()   
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said?", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action24')) or (a == self.myactions.get('action26')): #compliment_alone #ask_compliment_alone
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[10], natural_predicates)
                    natural_speech = natural_dict.get (a)
                    
                    if a == self.myactions.get('action24'):
                        behaviour = " and to express my " + self.personality + " personality"
                        sentence = openAI_client.start (natural_speech  + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action26'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    if a == self.myactions.get('action26'):
                        answ = self.ask_and_listen("Have you done what I've asked you?")
                        counter=0
                        while ("no" in str(answ)):
                            counter = counter+1
                            answ = self.ask_and_listen('Do that! I will really appreciate that. Have you done?')
                            if counter == 3 :
                                self.current_state = "state_one"
                                break 
                    # self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said?", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)


                if (a == self.myactions.get('action25')) or (a == self.myactions.get('action27')): #complimentfor_infrontof ask_complilmentfor_infrontof
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                    act = getcurrentstate2.find_action_by_index (grounded_terms[0])
                    natural_predicates = fromPredicates_toLanguage.fromPredicates_toLanguage (act)
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[9], natural_predicates)
                    natural_speech = natural_dict.get (a)
                    
                    if a == self.myactions.get('action25'):
                        behaviour = " and to express my " + self.personality + " personality"
                        sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    if a == self.myactions.get('action27'):
                        behaviour = " and to express my " + self.personality + " and persuasive personality"
                        sentence = openAI_client.start (' ask ' + natural_speech + natural_predicates + behaviour + self.language_sentence)
                        self.list_sentence.append (sentence+'\n')
                        volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                        self.audio.setOutputVolume(volume)
                        time.sleep(0.1)
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    # volume = 35 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    # self.audio.setOutputVolume(volume)
                    # time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(4)   
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    if a == self.myactions.get('action27'):
                        answ = self.ask_and_listen("Have you done what I've asked you?")
                        counter=0
                        while ("no" in str(answ)):
                            counter = counter+1
                            answ = self.ask_and_listen("Have you done? It will be so kind of you!!")
                            if counter == 3 :
                                self.current_state = "state_one"
                                # break 
                    result_checking_effects = self.check_predicates(self.expected_effects[i])
                    if not result_checking_effects:
                        self.ttsa.say("Have you understood what I've said?", self.configuration)
                        time.sleep (4)
                    self.add_or_replan (result_checking_effects)

                if (a == self.myactions.get('action28')) or (a == self.myactions.get('action29')) or (a == self.myactions.get('action30')) or (a == self.myactions.get('action31')) or (a == self.myactions.get('action32')) or (a == self.myactions.get('action33')) or (a == self.myactions.get('action34')) or (a == self.myactions.get('action35')): #test
                    # while self.queue.empty() or self.queue.get()=="Not-Updated":
                    #     time.sleep(1)
                    # if self.queue.get()=="Updated":
                        #act = getcurrentstate2.find_action_by_index ('test')
                    natural_dict=fromActions_toLanguage.fromActions_toLanguage ('ag1', 'ball', 'ag2', 'p2', 'test')
                    natural_speech = natural_dict.get (a)
                    behaviour = " and to express my " + self.personality + " personality"
                    sentence = openAI_client.start (natural_speech + behaviour + self.language_sentence)
                    self.list_sentence.append (sentence+'\n')
                    self.lock.acquire()
                    self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    self.lock.release ()
                    #self.predicates, self.pred_to_check, self.stablepred=self.mydatabase.read_from_database()
                    result_checking_preconditions = self.check_predicates(self.expected_preconditions[i])
                    self.add_or_replan (result_checking_preconditions)
                    volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
                    self.audio.setOutputVolume(volume)
                    time.sleep(0.2) 
                    self.ttsa.say (str(sentence), self.configuration)
                    time.sleep(1)   
                    # self.add_or_replan (result_checking_effects)
                    
                    self.done = True
                        
              
########################################AGGIUNGERE PER OGNI AZIONE EVENTUALI CONDIZIONI DI VOLUME E CONTROLLARE LE CONDIZIONI GROUNDED DI OGNI AZIONE, POTREBBERO ESERCI DEGLI ERRORI

            ########################### SE IL MONITORAGGIO DA ESITO NEGATIVO METTERE UN BREAK, COSi TORNA ALLO STATO ONE
            ##else:
                ##break
            if i < n_action-1:
                i=i+1
            else:
                print ('escooooooooooooo')
                break
        print (self.list_sentence)
        self.current_state = "state_one" #  HERE WE REPLAN OUR PLANNER BECAUSE THE ACTION IS NOT IN THE LIST