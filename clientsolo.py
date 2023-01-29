import requests
from collections import OrderedDict

url='http://127.0.0.1:5000/'
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

actions = OrderedDict  ([
        ('action1' , 'ask_go_out'),
        ('action2' , 'ask_move_obj'),
        ('action3' , 'ask_call_someone'),
        ('action4' , 'ask_someone_obj_place'),
        ('action5' , 'laugh')
        ])

my_plan = response_put.text
myplan2 = my_plan.replace("'", " ")
my_plan_3 = myplan2.replace('(', ' ')
my_plan_last = my_plan_3.replace(')', ' ')

my_plan_splitted = my_plan_last.split(' , ')
n_action=len(my_plan_splitted)
#print (my_plan_splitted[1])
my_string=my_plan_splitted[0].split(" ")
#print (my_string[3:len(my_string)-1]) #indici per avere i termini grounded del piano tipo [i][j] bisogna fare il match con le condizioni
#print (len (my_string))
my_new=[]
ind_action=[]
parameters=[]
for action in actions:
    for i, s in enumerate(my_domain_list):
        if actions.get(action) in s:
            ind_action.append(i+3)
            parameters.append (i+1)
for i, s in enumerate(my_domain_list):
    if 'effect ' in s:
        my_new.append(i-1)

my = []
for i in range(len(my_new)):
    my.append (my_domain_list [ind_action[i]:my_new[i]]) 

righe_parametri=[]
for i in (range(len (my))):    
    #print (my [i]) #lista delle precondizioni
    righe_parametri.append (my_domain_list[parameters[i]])
#print (righe_parametri) #lista dei parametri

print (my)
print (my[0][0])
print (righe_parametri[0])
print (my_string)
g=my[0][0]
myrep=['?x','?p']
j=0
for i in range (3,5):
    g= g.replace(myrep[j], my_string[i])
    j=j+1
print (g) 
##########FUNZIONA!!!!!! ADESSO FARLO PER TUTTI. BASTA FARE UN FOR IN MODO CHE MY POSSA CAMBIARE DA [0][0] SCORRERE GLI INDICI
######### COSI DA RIMPIAZZARE TUTTI I PARAMETRI