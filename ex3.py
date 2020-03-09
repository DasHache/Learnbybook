#programe pendu
import Tkinter as Tk
canvas = Tk.Canvas(width=200, height=200)
canvas.pack
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
        list_of_letters = ["_" if J1[i] not in lettres else J1[i] for i in range(len(J1))]
        string_from_list = ' '.join(list_of_letters)
        print '\n' + string_from_list.upper() + '\n'

    list_of_letters = ["_" if J1[i] not in lettres else J1[i] for i in range(len(J1))]
    guess = ''.join(list_of_letters)
    if guess == J1:
        print "You win!"
        break



# make the found value saved and write it somewhere
    if J1.find(J2) == -1 :
        if n-1> -1 :
            n = n-1
            if n == 9 :
                canvas.create_line(150, 190, 150, 20)
            if n == 8 :
                canvas.create_line(150, 20, 20, 20)

            print "Vous avez fait une faute, vous avez encore", n, "essaits"
        if n-1< 0 :
            print "Vous avez perdu, le mot etait",J1

            break

    canvas.pack()
    canvas.mainloop()

#print J1.ord(J2)                                                               

