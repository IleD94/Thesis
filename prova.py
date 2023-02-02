# Define problem  PUò ESSERE UNA FUNZIONE, O (UNA CLASSE) RENDERLA IL PIù PERSONALIZZABILE POSSIBILE!
prob1 = "(define \n    (problem test_prob)\n    (:domain"
test_dom="dominio_ciao"
mydom =  " "+ test_dom +") \n "
prob2 = "   (:objects \n"
myob1= "Antonio - person\n"
myob2 = "Ilenia - person\n"
myobjects= "        "+myob1 +"        "+myob2

prob3 = "    )\n    (:init\n"

pred1 = "(isIn Lorenzo)\n"
myinit =   "        "+pred1+"        (isIn Antonio)\n        (isIn Ilenia)\n        (ok)\n    )\n"    
           
prob4 = "    (:goal\n"

goal = "(ok)"
mygoal= "        "+goal    
           
prob5= "\n    )  \n)  "

problem = prob1+mydom+prob2+myobjects+prob3+myinit+prob4+mygoal+prob5
print (problem) 

# Write PDDL files

with open("problema.pddl", "w") as f:
    f.write(problem)