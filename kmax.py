n = input()
k = input()
k = eval(k)
i = 0
ii = 0
n = eval(n)
k2 = n
i1 = 0
i2 = 1
i3 = 2

num = 0

l = []

while i != n:
    l.append(input())
    i += 1
    if i == n:
        break
# will complete later for series lesser than 3

while ii < n * n:
    if l[i2] <= l[i3]:
        num = l[i2]
        l[i2] = l[i3]
        l[i3] = num
        if l[i1] <= l[i2]:
            num = l[i1]
            l[i1] = l[i2]
            l[i2] = num
            if l[i2] <= l[i3]:
                num = l[i2]
                l[i2] = l[i3]
                l[i3] = num
    if l[i1] <= l[i2]:
        num = l[i1]
        l[i1] = l[i2]
        l[i2] = num
        if l[i2] <= l[i3]:
            num = l[i1]
            l[i1] = l[i2]
            l[i2] = num
            if l[i1] <= l[i2]:
                num = l[i1]
                l[i1] = l[i2]
                l[i2] = num
    if l[i1] <= l[i3]:
        num = l[i2]
        l[i2] = l[i3]
        l[i3] = num
        if l[i2] <= l[i3]:
            num = l[i1]
            l[i1] = l[i2]
            l[i2] = num
            if l[i1] <= l[i2]:
                num = l[i2]
                l[i2] = l[i3]
                l[i3] = num
    if l[i3] <= l[i2] <= l[i1] and i3 == n - 1:
        i1 = 0
        i2 = 1
        i3 = 2
    if l[i3] <= l[i2] <= l[i1]:
        i1 += 1
        i2 += 1
        i3 += 1
        ii += 1





print(l[k])
print(l)

# while k2 != k:


# while i != n:
#     if i != n-1:
#         if eval(n1) > eval(n2):
#             n2 = input()
#             i += 1
#         elif eval(n1) == eval(n2):
#             n2 = input()
#             i += 1
#         elif eval(n1) < eval(n2):
#             n1 = n2
#             n2 = input()
#             i += 1
#     else:
#         print(n1)
#         break
#
