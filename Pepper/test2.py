#! /usr/bin/env python3

from flask import Flask, request
import os
import shutil
import subprocess
import textwrap
import json
import time

app = Flask(__name__)

@app.route ('/planner_launch', methods = ['PUT'] )

def get_domain():
    mydata = request.get_json()
    domain = mydata['domain']
    json_string=json.dumps(domain, indent=4)
    json_string_virg = json_string.replace('"','  ')
    json_string_square1 = json_string_virg.replace(',','  ')
    json_string_square2 = json_string_square1.replace('[','')
    json_string_final = json_string_square2.replace(']','')
    mydomain = str(domain)
    if os.path.isfile('domain.pddl'):
        os.remove('domain.pddl')
    f = open ('domain.pddl', 'w')
    f.write (json_string_final)
    f.close()
    problem = mydata['problem']
    json_string=json.dumps(problem, indent=4)
    json_string_virg = json_string.replace('"','  ')
    json_string_square1 = json_string_virg.replace(',','  ')
    json_string_square2 = json_string_square1.replace('[','')
    json_string_final = json_string_square2.replace(']','')
    myproblem = str(problem)
    if os.path.isfile('problem.pddl'):
        os.remove('problem.pddl')
    f = open ('problem.pddl', 'w')
    f.writelines (json_string_final)
    f.close()
    mydir = 'C:\Users\Lemonsucco\Desktop\Pepper\\'
    print (mydir)
    planner_path = 'C:\Users\Lemonsucco\Desktop\downward-main'
    os.chdir (planner_path)
    shutil.copyfile(mydir+'\domain.pddl', planner_path+"\domain.pddl")
    shutil.copyfile(mydir+'\problem.pddl', planner_path+"\problem.pddl")
    command = ".\fast-downward.py --portfolio-single-plan --portfolio-bound=20 --alias seq-sat-fdss-2018 \
        --overall-time-limit 30m  domain.pddl problem.pddl" 
    #run the planner
    fd_process = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = fd_process.communicate()
    fd_exit = fd_process.returncode
    shutil.copyfile(planner_path+'\sas_plan', mydir+"\sas_plan")
    output_path = mydir+"\sas_plan"
    #print (fd_exit)
    if os.path.isfile(output_path):
        plan_file = open(output_path, "r")
        raw_plan = plan_file.readlines()
        plan_file.close()
        my_plan= str(raw_plan)
        print (raw_plan)
        if 'recognize' in my_plan:
            print ("sono dentro")
        if 'say_something' in my_plan:
            print ("lallero")
        resp = {'plan': raw_plan,
                'message': 'The planner found a solution.'}
    return (my_plan)
    
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)