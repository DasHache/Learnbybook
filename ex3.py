#programe pendu                                                                  
J1 = raw_input("joueur 1, donnez le mot a deviner ")
x = len(J1)
n = 10
print "le mot contient", x,"lettres, vous aurez le droit a 10 erreurs"
while n > -1 :
    J2 = raw_input("joueur 2, donnez la lettre a essayer")
    if J1.find(J2) > -1 :    
        print "la lettre est presente", J1.count(J2), "fois, a la",[i+1 for i in range(len(J1)) if J1[i] == J2], "eme place"
        print ["_" if J1[i] != J2 else J2 for i in range(len(J1))]
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

