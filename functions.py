from collections import OrderedDict
#import re

def find_all_indices(string, char):
    indices = []
    index = -1
    while True:
        index = string.find(char, index+1)
        if index == -1:
            break
        indices.append(index)
    return indices



def find_expected_predicates(action, domain, mydict, my_string):

    ind_effects=[]
    ind_action=[]
    parameters=[]

    for i, s in enumerate(domain):
        if mydict.get(action) in s:
            ind_action.append(i+3)
            parameters.append (i+1)
        if 'effect ' in s:
            ind_effects.append(i-1)

    my_precondition = []
    my_action = ind_action[0]
    my_effect = ind_effects[0]
    #for i in range(len(ind_effects)):
    my_precondition.append (domain [])

    righe_parametri=[]
    #for i in (range(len (my_precondition))):    
        #print (my [i]) #lista delle precondizioni
    righe_parametri= domain[parameters]
    #print (righe_parametri) #lista dei parametri
    print (righe_parametri)
    print (my_precondition)
    #print (righe_parametri[0])
    print (my_string)

    f=[]
    for i in (range(len (righe_parametri))):
        f.append(find_all_indices(righe_parametri[i], '?'))
    print(f)
    return f
    # mychar=righe_parametri[0]

    # my_param=[]
    # for ind in f:
    #     my_param.append(mychar[ind+1])
    # print (my_param)
    # g=my_precondition[0][0]
    # j=0
    # for i in range (3,5):
    #     g=g.replace(my_param[j], my_string[i])
    #     j=j+1
    
    # return g