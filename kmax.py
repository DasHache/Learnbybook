

n = input()
k = input()
i = 1
n1 = input()
n2 = input()
n = eval(n)

while i != n:
    if i != n-1:
        if eval(n1) > eval(n2):
            n2 = input()
            i += 1
        elif eval(n1) == eval(n2):
            n2 = input()
            i += 1
        elif eval(n1) < eval(n2):
            n1 = n2
            n2 = input()
            i += 1
    else:
        print(n1)
        break




