#program pendu                                                                  
J1 = raw_input("joueur 1, donnez le mot a deviner ")
x = len(J1)
n = 10
print "le mot contient", x,"lettres, vous aurez le droit a 10 erreurs"
while True :
    J2 = raw_input("joueur 2, donnez la lettre a essayer")
    if J1.find(J2) > -1 :    
        print "la lettre est presente", J1.count(J2), "fois, a la",[i+1 for i in range(len(J1)) if J1[i] == J2], "eme place"
    if J1.find(J2) == -1 :
        if n-1> 0 :
            n=n-1
            print "vous avez fait une faute, vous avez encore", n, "essaits"
        if n-1< 0 :
            print "vous avez perdu, le mot etait",J1
            
            Break    
#print J1.ord(J2)                                                               

