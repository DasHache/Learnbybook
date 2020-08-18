n = input()
i = 0
c = 1
s1 = input()
s2 = input()

while i < eval(n):
    if s1 == s2:
        c += 1
    else:
        print(s1, " ", c)
        c = 1
    s1 = s2
    if i < eval(n) - 2:
        s2 = input()
    i += 1
    if i == eval(n) - 1:
        break
print(s1, " ", c)
quit()



