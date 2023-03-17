#! /usr/bin/env python3

from flask import Flask, request
import os
import shutil
import subprocess
import json
import time
from pddlpy import DomainProblem

app = Flask(__name__)

@app.route ('/planner_launch', methods = ['PUT'] )

def get_domain():
    planner_path = "/root/Desktop/downward-main/"
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
    with open (planner_path+'domain.pddl', 'w') as f:
        f.write(json_string_final)
    problem = mydata['problem']
    json_string=json.dumps(problem, indent=4)
    json_string_virg = json_string.replace('"','  ')
    json_string_square1 = json_string_virg.replace(',','  ')
    json_string_square2 = json_string_square1.replace('[','')
    json_string_final = json_string_square2.replace(']','')
    myproblem = str(problem)
    if os.path.isfile('problem.pddl'):
        os.remove('problem.pddl')
    with open (planner_path+'problem.pddl', 'w') as f:
        f.write(json_string_final)
    mydir = "/root/Desktop/test_Pepper"
    print (mydir)
    os.chdir (planner_path)
    #shutil.copyfile(mydir+'/domain.pddl', planner_path+"/domain.pddl")
    #shutil.copyfile(mydir+'/problem.pddl', planner_path+"/problem.pddl")
    command = "./fast-downward.py --portfolio-single-plan --portfolio-bound=20 --alias seq-sat-fdss-2018 \
        --overall-time-limit 30m  domain.pddl problem.pddl" 
    #run the planner
    fd_process = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = fd_process.communicate()
    fd_exit = fd_process.returncode
    shutil.copyfile(planner_path+'/sas_plan', mydir+"/sas_plan")
    output_path = mydir+"/sas_plan"
    print (fd_exit)
    if os.path.isfile(output_path):
        with open(output_path, "r") as plan_file:
            raw_plan = plan_file.readlines()
        my_plan= str(raw_plan)
        print (raw_plan)
        

    # Load the domain file
    with open("domain.pddl", "r") as f:
        domain = DomainProblem.parse_pddl_domain(f)

    # Load the problem file
    with open("problem.pddl", "r") as f:
        problem = DomainProblem.parse_pddl_file(f, domain)

    # Access domain properties
    print("Domain name:", domain.name)
    print("Actions:", domain.actions)

    # Access problem properties
    print("Problem name:", problem.name)
    print("Initial state:", problem.init)
    print("Goal:", problem.goal)

    return (my_plan)
    
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)