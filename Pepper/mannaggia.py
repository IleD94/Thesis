flag = True
while flag:
        id=raw_input ("Who are you?")


        if id == "nano barbuto morsuto":
            NBMorsuto = True
            Lemonsucco = False
            flag = False
        elif id == "lemonsucco":
            Lemonsucco = True
            NBMorsuto = False
            flag = False
        else:
            print ("Sorry, you're not in my database, try with another name")
            Lemonsucco = False
            NBMorsuto = False
        if Lemonsucco:
            Love='N.B.Morsuto'
        if NBMorsuto:
            Love='Lemonsucco'

print ("Love is... " + Love  )