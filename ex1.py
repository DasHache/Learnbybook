from random import randint
#x = input("quel est la date de naissance de Alberts Einstein?")
#if 1976 <= x <= 1986 :
#    print "vous avez raison."
#else :
#    print "espece d'inculte!"
x = raw_input("Voulez vous jouez a feuille, caillou et ciseaux ?")
if x == "non" :
    print "D'accords, merci et au revoir !"
else : 
   # 1 == "feuille"
    #2 == "caillou"
    #3 == "ciseaux"
    o = randint(1,3)
    
    if o  == 1 :
        o == "feuille"
    elif o  == 2 :
        o == "caillou"
    elif o  == 3 :
        o == "ciseau"
        
    j = raw_input("choisissez soit la feuille, soit le caillou, soit le ciseaux")
    print "oki"
    if j == "ciseaux" :
        if o == "ciseaux" :
            print "egalite"
        elif o == "feuille" :
            print "victoire"
        elif o == "caillou" :
            print "defaite"
    elif j == "feuille" :
        if o == "caillou" :
            print "victoire"
        elif o == "feuille" :
            print "egalite"
        elif o == "ciseau" :
            print "defaite"
    elif j == "caillou" :
        if o == "caillou" :
            print "egalite"
        elif o == "feuille" :
            print "defaite"
        elif o == "ciseau" :
            print "egalite"
    print "bite"
