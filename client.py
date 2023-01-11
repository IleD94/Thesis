import requests
import sys

url='http://127.0.0.1:5000/'
    
mydir = "C:\Users\Lemonsucco\Desktop\Pepper\\"
domain_path = mydir+sys.argv[1]
my_domain_list=[]
with open (domain_path, "r") as f:
    for line in f:
        my_domain_list.append(line.strip())
#print (my_domain_list)
#data = {'domain':my_domain}
problem_path = mydir+sys.argv[2]
my_problem_list=[]
with open (problem_path, "r") as f:
    for line in f:
        my_problem_list.append(line.strip())
#print (my_problem_list)
#data2 = {'problem':my_problem}
headers= {'Content-Type':'application/json'}
response_put1 = requests.put(url+'domain', json=my_domain_list)
print(response_put1.status_code)
response_put1 = requests.put(url+'problem', json=my_problem_list, headers=headers)
print(response_put1.status_code)