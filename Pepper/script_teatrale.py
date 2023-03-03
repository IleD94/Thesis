import getcurrentstate
import fromActions_toLanguage
import openAI_client
personality = 'histrionic'
myactions, myplan =getcurrentstate.start()
# sentence_list = []
# language = 'Italian'
# n_action=len (myplan)-1
# i=0
# for action in myactions:
#     #print(action)
#     u=myplan[i].split()
#     if i==0 or (i==n_action):
#         a=u[1]
#         grounded_terms= u[2:len(u)-1]
#     else:
#         a=u[0]
#         grounded_terms= u[1:len(u)-1]
#     if a in myactions.values() :
#         print(a)
#         # if (a == myactions.get('action25')) or (a == myactions.get('action27')): #complimentfor_infrontof ask_complilmentfor_infrontof
#         #         # while self.queue.empty() or self.queue.get()=="Not-Updated":
#         #         #     time.sleep(1)
#         #         # if self.queue.get()=="Updated":
#         #         act = getcurrentstate.find_action_by_index (grounded_terms[2])
#         #         natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[8], 'ball', grounded_terms[7], grounded_terms[9], act)
#         #         natural_speech = natural_dict.get (a)
#         #         if action == "action25":
#         #             behaviour = "and to express my " + personality + " personality"
#         #             sentence = openAI_client.start ('ask' + natural_speech + behaviour+ 'Say that in '+ language)
#         #             sentence_list.append(sentence)
#         if (a == myactions.get('action3')) or (a == myactions.get('action4')): #Ask_Put_inFrontOf #Ask_Put_inFrontOf_Manipulative 
#                 # while self.queue.empty() or self.queue.get()=="Not-Updated":
#                 #     time.sleep(1)
#                 # if self.queue.get()=="Updated":
#                 natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[7], grounded_terms[12], grounded_terms[8], grounded_terms[11],a)
#                 natural_speech = natural_dict.get (a)
#                 if action == "action3":
#                     behaviour = "and to express my " + personality + " personality"
#                     sentence = openAI_client.start ('ask' + natural_speech + behaviour+ 'Say that in '+ language)
#                     sentence_list.append(sentence)
#         if (a ==myactions.get('action5')) or (a == myactions.get('action6')) or (a == myactions.get('action7')) or (a == myactions.get('action8')): #Ask_Go #Ask_Go_Manipulative #Ask_Comeback #Ask_Comeback_Manipulative
#                 print ("RICONOSCO L'AZIONE")
#                 print (a)
#                 print (myactions.get('action6'))
#                 print (action)
#                 # while self.queue.empty() or self.queue.get()=="Not-Updated":
#                 #     time.sleep(1)
#                 # if self.queue.get()=="Updated":
#                 natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[7], grounded_terms[9],a)
#                 natural_speech = natural_dict.get (a)
#                 if a == myactions.get('action5'):
#                     behaviour = " and to express my " + personality + " personality"
#                     sentence = openAI_client.start (' ask ' + natural_speech + behaviour + 'Say that in '+ language)
#                     sentence_list.append(sentence)
#         if (a ==myactions.get('action1')) or (a == myactions.get('action2')): #Ask_Put_Alone #Ask_Put_Alone_Manipulative  
#                 # while self.queue.empty() or self.queue.get()=="Not-Updated":
#                 #     time.sleep(1)
#                 # if self.queue.get()=="Updated":
#                 natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[10], grounded_terms[16], grounded_terms[11], grounded_terms[15],a)
#                 natural_speech = natural_dict.get (a)
#                 print (natural_speech)
#                 if action == "action1":
#                     behaviour = "and to express my " + personality + " personality. "
#                     sentence = openAI_client.start ('ask' + natural_speech + behaviour + ' Say that in '+ language)
#                     sentence_list.append(sentence)
#         # if (a ==myactions.get('action9')): #tell_alone
#         #         # while self.queue.empty() or self.queue.get()=="Not-Updated":
#         #         #     time.sleep(1)
#         #         # if self.queue.get()=="Updated":
#         #         act = getcurrentstate.find_action_by_index (grounded_terms[0])
#         #         natural_dict=fromActions_toLanguage.fromActions_toLanguage (grounded_terms[6], 'ball', grounded_terms[5], grounded_terms[8], act)
#         #         natural_speech = natural_dict.get (a)
#         #         behaviour = " and to express my " + personality + "personality."
#         #         sentence = openAI_client.start (natural_speech + behaviour + ' Say that in '+ language)
#         #         sentence_list.append(sentence)
#         if (a == myactions.get('action28')): #test
#                 # while self.queue.empty() or self.queue.get()=="Not-Updated":
#                 #     time.sleep(1)
#                 # if self.queue.get()=="Updated":
#                     #act = getcurrentstate.find_action_by_index ('test')
#                 natural_dict=fromActions_toLanguage.fromActions_toLanguage ('ag1', 'ball', 'ag2', 'p2', 'test4')
#                 natural_speech = natural_dict.get (a)
#                 behaviour = " and to express my " + personality + " personality and being a successful person"
#                 sentence = openAI_client.start (natural_speech + behaviour + ' Say that in '+ language)
#                 sentence_list.append(sentence)
#     if i < n_action-1:
#         i=i+1
# print (sentence_list)