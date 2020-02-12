#program pendu                                                                  
J1 = raw_input("joueur 1, donnez le mot a deviner ")
x = len(J1) 
print "le mot contient", x,"lettres"
J2 = raw_input("joueur 2, donnez la lettre a essayer, vous avez le droit a 10 erreurs ")
print "la lettre est presente", J1.count(J2), "fois, a la", str([i+1 for i in range(len(J1)) if J1[i] == J2]), "eme place"

#print J1.ord(J2)                                                               

