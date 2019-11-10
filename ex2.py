#juste prix
from random import randint

x = randint(30,100)
print x
n = 2 
y = raw_input("Vous allez jouer a juste prix, donc vous devez deviner le prix d un objet compris entre 30 et 100 francs. Combien selon vous coute l objet ?")
if y>x :
    y = raw_input("c'est moins. Combien?")
elif y<x :
    y = raw_input("c'est plus. Combien?")
else :
    print "Vous avez gagne!"
        
#if  y > x :
 #   print "c'est plus"
  #  y = raw_input("encore?")
   # print x
#if  y < x :
 #   print "c'est moins"
  #  y = raw_input("encore?")
   # print x
#if x == y :
 #   print "Vous avez gagne"
        
