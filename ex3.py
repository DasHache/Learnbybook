#programe pendu
#import Tkinter as Tk
#canvas = Tk.Canvas(width=200, height=200)
#canvas.pack
J1 = raw_input("Joueur 1, donnez le mot a deviner: \n")
x = len(J1)
n = 10
print "Le mot contient", x,"lettres, vous aurez le droit a 10 erreurs!"
lettres = [] # 1. Keep all entered letters in this array
while n > -1 :
    J2 = raw_input("Joueur 2, donnez la lettre a essayer: \n")
    lettres.append(J2) # 2. Add a new entered letter into the array
    if J1.find(J2) > -1 :    
        print "La lettre est presente", J1.count(J2), "fois, a la", ', '.join([str(i+1) for i in range(len(J1)) if J1[i] == J2]), "eme place"
        # 3. Python operator 'in'
        # 'in' is a Python operator, it means 'element is contained in the array'
        # 1 in [1,2,3] - returns TRUE
        # 1 not in [1,2,3] - return the opposite - FALSE

        # 4. A result of a LIST COMPREHENSION is... a LIST! suprise?
        # When Python prints a LIST it prints each element separated by a comma, surrounded by square brackets
        # So, you need to COVERT a list into a string:
        # How to make a string:
        list_of_letters = ["_" if J1[i] not in lettres else J1[i] for i in range(len(J1))]
        string_from_list = ' '.join(list_of_letters)
        # 5. For details, see: https://docs.python.org/2/library/stdtypes.html#str.upper
        print '\n' + string_from_list.upper() + '\n'
       # for i in range(len(J1)) :
        #    if J1[i] == J2 :
         #       print [J2]
          #  else :
           #     print ("_")
            
                       
    if J2 == J1 :
        print "You win!"
        break

# make the found value saved and write it somewhere
    if J1.find(J2) == -1 :
        if n-1> -1 :
            n=n-1
        
            print "Vous avez fait une faute, vous avez encore", n, "essaits"
        if n-1< 0 :
            print "Vous avez perdu, le mot etait",J1
            n=n-1
            
            
        
#print J1.ord(J2)                                                               

