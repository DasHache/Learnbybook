#programe pendu                                                                  
J1 = raw_input("joueur 1, donnez le mot a deviner ")
x = len(J1)
n = 10
print "le mot contient", x,"lettres, vous aurez le droit a 10 erreurs"
lettres = [] # 1. Keep all entered letters in this array
while n > -1 :
    J2 = raw_input("joueur 2, donnez la lettre a essayer")
    lettres.append(J2) # 2. Add a new entered letter into the array
    if J1.find(J2) > -1 :    
        print "la lettre est presente", J1.count(J2), "fois, a la",[i+1 for i in range(len(J1)) if J1[i] == J2], "eme place"
        # 3. Python operator 'in'
        # 'in' is a Python operator, it means 'element is contained in the array'
        # 1 in [1,2,3] - returns TRUE
        # 1 not in [1,2,3] - return the opposite - FALSE
        print ["_" if J1[i] not in lettres else J1[i] for i in range(len(J1))]
       # for i in range(len(J1)) :
        #    if J1[i] == J2 :
         #       print [J2]
          #  else :
           #     print ("_")
            
                       
    if J2 == J1 :
        print "you won"
        break

# make the found value saved and write it somewhere
    if J1.find(J2) == -1 :
        if n-1> -1 :
            n=n-1
        
            print "vous avez fait une faute, vous avez encore", n, "essaits"
        if n-1< 0 :
            print "vous avez perdu, le mot etait",J1
            n=n-1
            
            
        
#print J1.ord(J2)                                                               

