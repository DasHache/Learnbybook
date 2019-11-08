#juste prix
from random import randint

x = randint(30,100)
print x
y = raw_input("Vous allez jouer a juste prix, donc vous devez deviner le prix d un objet compris entre 30 et 100 francs. Combien selon vous coute l objet ?")

if y > x :
    print "c'est moins"
    y = raw_input("encore?")
    print x
elif y < x :
    print "c'est plus"
    y = raw_input("encore?")
    print x
if x == y :
    print "Vous avez gagne"
