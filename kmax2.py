n = input()
n = eval(n)
k = input()
k = eval(k)
l = []
i = 0
while i < n:
    l += [input()]
    i += 1
    if i == n:
        break
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

    if i == n * n:
        break

print(l[k])
print(l)
l.sort(reverse=True)
print(l)
