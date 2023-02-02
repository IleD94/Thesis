import requests
from collections import OrderedDict

def find_all_indices(string, char):
    indices = []
    index = -1
    while True:
        index = string.find(char, index+1)
        if index == -1:
            break
        indices.append(index)
    return indices

def grounded_terms(my_string):
    groundedterms = my_string[3:len(my_string)-1]
    return groundedterms

def get_my_precondition (parameter_string):
    ind_param_question_mark = find_all_indices(parameter_string, '?') 
    get_my_param=[]
    
    for i in ind_param_question_mark:
        j=i+2
        while parameter_string[j] != ' ':
            j=j+1
        get_my_par= (parameter_string[i:j])
        get_my_param.append (get_my_par)
    return get_my_param
    

def get_expected_precondition(precondition_list, groundedterms,myparams, result): 
    expected_precondition_list = []
    for i in range(len(precondition_list)):
        precondition = precondition_list[i]
        h=result[i]
        groundedterm = groundedterms[h]
        myparam = myparams[i]
        #print (precondition[-1])
        expected_precondition = []
        # print (myparam)
        # print (groundedterm)
        for j in range(len(precondition)):
            pre = precondition[j]
            # if '?' not in (pre):
            #     expected_precondition.append(pre)
            #     expected_precondition_list.append(expected_precondition)
            #     break
            # else:
            for k in range(len(myparam)): 
                pre = pre.replace(str(myparam[k]), str(groundedterm[k]))
            expected_precondition.append(pre)
        expected_precondition_list.append(expected_precondition)
    return expected_precondition_list



url='http://127.0.0.1:5000/'
mydir = "C:\Users\Lemonsucco\Desktop\Pepper\\"
domain_path = mydir+'thesis_domain3.pddl'
my_domain_list=[]
with open (domain_path, "r") as f:
    for line in f:
        my_domain_list.append(line.strip())
problem_path = mydir+'thesis_problem3.pddl'
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

actions = OrderedDict  ([
        ('action1' , 'ask_put_alone'),
        ('action2' , 'ask_put_alone_manipulative'),
        ('action3' , 'ask_put_infrontof'),
        ('action4' , 'ask_put_infrontof_manipulative'),
        ('action5' , 'ask_go'),
        ('action6' , 'ask_go_manipulative'),
        ('action7' , 'ask_comeback_manipulative'),
        ('action8' , 'ask_comeback'),
        ('action9' , 'tell_alone'),
        ('action10' , 'tell_everybody'),
        ('action11' , 'tell_infrontof'),
        ('action12' , 'insult_alone'),
        ('action13' , 'insult_infrontof'),
        ('action14' , 'ask_insult_alone'),
        ('action15' , 'ask_insult_infrontof'),
        ('action16' , 'praise_alone'),
        ('action17' , 'praise_infrontof'),
        ('action18' , 'ask_praise_alone'),
        ('action19' , 'ask_praise_infrontof'),
        ('action20' , 'blamefor_alone'),
        ('action21' , 'blamefor_infrontof'),
        ('action22' , 'ask_blamefor_alone'),
        ('action23' , 'ask_blamefor_infrontof'),
        ('action24' , 'complimentfor_alone'),
        ('action25' , 'complimentfor_infrontof'),
        ('action26' , 'ask_complimentfor_alone'),
        ('action27' , 'ask_complimentfor_infrontof'),
        ('action28' , 'test')
        ])


my_plan = response_put.text
#print (my_plan)
myplan2 = my_plan.replace("'", " ")
my_plan_3 = myplan2.replace('(', ' ')
my_plan_last = my_plan_3.replace(')', ' ')

my_plan_splitted = my_plan_last.split(' , ')
n_action=len(my_plan_splitted)-1
#print(n_action)
#print (my_plan_splitted[1])
my_string=[]
for i in range (0,n_action):
    #print(i)
    
    my_string.append (my_plan_splitted[i].split(" "))

#print (my_string)

groundedterms=[]
for i in range(len(my_string)):
    groundedterms.append(grounded_terms(my_string[i]))
    
#print (groundedterms) #sono i termini grounded in ordine per azione lista di liste
actions_plan=[]
i=0
for action in actions:
            
    u=my_plan_splitted[i].split()
    
    if i==0 or (i==n_action):
        a=u[1]
        #print(a)
        
    else:
        a=u[0]

    
    #print (actions.get(action))
    #print (actions.values())
    if a in actions.values() :
        actions_plan.append (a)
    if i< n_action:
        i=i+1
    else:
        break
                
# print (actions_plan)
# print (my_plan_splitted)
ind_precod_list_start=[]
ind_parameters=[]
ind_precod_list_end=[]
my_actions=[]
j=[]
actions_list=[]
ind_effect_list_start=[]
ind_effect_list_end=[]
k=0
#print(my_plan)
current_action = None
for i, s in enumerate(my_domain_list):
    for action in actions:

        #print(action)
        if 'action' in s:
            o=s.lower()
            a=o.split(' ')
            #print (a[1])    
            if (actions.get(action) == a[1]) and (actions.get(action) in my_plan):
                #print('CI ENTROOOOOOOOOOOOOOOOOOOOOO')
                #print (s.lower())
                ind_precod_list_start.append(i+3)
                ind_parameters.append(i+1)
                current_action = action
                actions_list.append(a[1])
                
                #print (current_action)
                break
    if ('effect ' in s) and (current_action is not None):
        ind_precod_list_end.append(i-1)
        ind_effect_list_start.append (i+1)
        current_action = None
    # print(len(ind_effect_list_start))

    

# print (actions_list)
k=0
for i, s in enumerate(my_domain_list):
    if (';end_effect'in s) and (i >= ind_effect_list_start [k]):
        ind_effect_list_end.append(i)
        if k<len(ind_effect_list_start):
            k=k+1
# print (ind_effect_list_start)
# print (ind_effect_list_end)
# print (my_domain_list[1558])
#print (my_actions)
#print(ind_precod_list_start) #lista inizio precondizioni
#print(ind_precod_list_end) #lista fine precondizioni
# print (ind_parameters) #lista delle righe dei parametri

effects_list=[]
precondition_list=[]
#print (precondition_list)
parameters_list=[]
#print (parameters_list)
for i in range(n_action):
    
    if (ind_precod_list_start[i]==ind_precod_list_end[i]):
        precondition_list.append(my_domain_list[ind_precod_list_start[i]])
    else:
        precondition_list.append(my_domain_list[ind_precod_list_start[i]: ind_precod_list_end[i]])

    if (ind_effect_list_start[i]==ind_effect_list_end[i]):
        effects_list.append (my_domain_list[ind_effect_list_start[i]])
    else:
        effects_list.append (my_domain_list[ind_effect_list_start[i]:ind_effect_list_end[i]])
    parameters_list.append(my_domain_list[ind_parameters[i]])
        

#print (effects_list)

# print (parameters_list)
my_params=[]
for parameter_string in (parameters_list):
    #print (parameter_string)
    mypar=get_my_precondition(parameter_string)
    my_params.append (mypar)
# print (my_params)



#print (precondition_list)

result = []
for element in actions_list:
    if element in actions_plan:
        result.append(actions_plan.index(element))
# print(result)


####### Fare la sostituzione etnica dei termini nella precondition list, con i termini grounded tenendo conto 
######## di matchare i  parametri con i termini grounded parm [i] ground[i] stesso indice (si puo' fare)
#
expected_precondition_list=[]
i=0
#print (groundedterms)
#print (my_params)

expected_precondition_list = get_expected_precondition(precondition_list, groundedterms, my_params, result)
expected_effects_list= get_expected_precondition (effects_list, groundedterms, my_params, result)
print (expected_precondition_list) #sono messe nell'ordine del dominio, non nell'ordine del piano, ricordatelo. forse conviene metterle nell'ordine del piano, capire come fare
print (expected_effects_list) #forse si può fare riutilizzando gli indici della lista delle azioni nel piano e mettendo le precondizioni e gli effetti in quell'ordine

# si potrebbe fare un dizionario con due campi per ogni azione che viene trovata dal piano (anche con ordine diverso)
#si potrebbe fare una lista con il numero di azione nell'ordine in cui viene trovato (è mezzo fatto già forse) e poi utilizzarlo come chiave del dizionario
#e associarci gli indici degli effetti e delle precondizioni. Capire come unire il modulo al codice