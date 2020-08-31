n = input("length of the list, the number of numbers you have to enter\n")
n = eval(n)
k = input("the index of the greatest number, the bigger it is the lesser the number will be \n")
k = eval(k)
l = []
i = 0
while i < n:
    l += [int(input("enter a number\n"))]
    i += 1

i = 0
i1 = 0
num = 0
while i != n * n:
    if l[i1] < l[i1 + 1]:
        num = l[i1]
        l[i1] = l[i1 + 1]
        l[i1 + 1] = num
        i1 += 1

    if i1 != n - 1 and l[i1] >= l[i1 + 1]:
        i1 += 1

    if i1 == n - 1:
        if l[i1] > l[i1 - 1]:
            num = l[i1 - 1]
            l[i1 - 1] = l[i1]
            l[i1] = num
        i1 = 0
        i += 1


print(l[k])
