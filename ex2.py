#juste prix

from random import randint

def justeprix() :
    x = randint(30,100)
    print x 
    y = raw_input("Vous allez jouer a juste prix, donc vous devez deviner le prix d un objet compris entre 30 et 100 francs en 10 tentative. Combien selon vous coute l objet ?")
    t = 0
    t = t+1
    print "tentative numero", t
    if y == "code triche" :
        print x
    else :
        y_int = int(y)
        while t<10 :
            if t == 5 :
                print "attention, plus que 5 essais"
            if x<y_int :
                y = raw_input("c'est moins. Combien?")
                t = t+1
                print "tentative numero", t
            if x>y_int :
                y = raw_input("c'est plus. Combien?")
                t = t+1
                print "tentative numero", t
            if t == 10 :
                print "vous avez perdu, la reponse etait", x
            #r = raw_input("voulez vous rejouer?")
            else :
                print "Vous avez gagne!"
            #r = raw_input("voulez vous rejouer?")
                break
        
justeprix()
r = raw_input("voulez vous rejouer?")
#r = raw_input("voulez vous rejouer?")
while True :
    if r == "oui":
        justeprix()
        r = raw_input("voulez vous rejouer?")
    else :
        break
