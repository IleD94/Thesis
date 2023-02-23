import qi
import argparse
import sys
import requests
import time
from fsm2 import StateMachine
from collections import OrderedDict

if __name__ == "__main__":

    url='http://127.0.0.1:5000/'
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="130.251.13.141",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    
    parser.add_argument(sys.argv[1])

    parser.add_argument(sys.argv[2])
    args = parser.parse_args()
    
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n")
        print("Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    tts = session.service("ALTextToSpeech")
    mydir = "C:\Users\Lemonsucco\Desktop\Pepper\\"
    domain_path = mydir+sys.argv[1]
    my_domain_list=[]
    with open (domain_path, "r") as f:
        for line in f:
            my_domain_list.append(line.strip())
    #response_put= requests.put(url+'planner_launch', json=my_domain_list)
    #print(response_put.status_code)
    problem_path = mydir+sys.argv[2]
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
    print(response_put.status_code)
    #time.sleep ()
    #response_get = requests.get(url+'planner_launch')
    my_plan = response_put.text
    
    actions = OrderedDict  ([
    ('action1', 'see_infer_know'),
    ('action2', 'know_another_isin'),
    ('action3', 'one_see_another'),
    ('action4' , 'agent_know_isputting'),
    ('action5' , 'isputting_infer_see'),
    ('action6' , 'know_isputting_infer_know_isin'),
    ('action7' , 'know_iamputting_infer_know_isin'),
    ('action8' , 'know_isgoing_infer_know'),
    ('action9' , 'know_isin_infer_know_isgoing'),
    ('action10' , 'know_isgoing_afterphase'),
    ('action11' , 'know_iamgoing_afterphase'),
    ('action12' , 'test')
    ])
    
    myplan2 = my_plan.replace("'", " ")
    my_plan_3 = myplan2.replace('(', ' ')
    my_plan_last = my_plan_3.replace(')', ' ')

    my_plan_splitted = my_plan_last.split(' , ')
    n_action=len(my_plan_splitted)
    print(my_plan_last)
    print (n_action)
    i=0
    time.sleep(5)
    for action in actions:
       # print (actions.get(action))
        print (my_plan_splitted[i])
        #print (len(my_plan_splitted))
        u=my_plan_splitted[i].split()
        if i==0 or (i==n_action-1):
            a=u[1]
        else:
            a=u[0]
        print (u)
        if a in str(actions) :
            n = my_plan.count(actions.get(action))
            print (n)
            tts.say(a)
        if i< n_action-1:
           i=i+1
            #print (actions.get(action))
            #for j in range (0,n):
                
            

    #print(len(my_plan_splitted))
        
    print (my_plan)