#program pendu                                                                  
J1 = raw_input("joueur 1, donnez le mot a deviner ")
x = len(J1) + 1
print "le mot contient", x,"lettres"
J2 = raw_input("joueur 2, donnez la lettre a essayer, vous avez le droit a 10 e\
rreurs ")
print "la lettre est presente", J1.count(J2), "fois, a la", J1.find(J2)+1, "eme\
 place"
#print J1.ord(J2)                                                               

