n = int(input("enter the number of mouses\n"))
l = []
i = 0
while i < n:
    l.append(int(input("enter the number of the party for which the mouse has voted\n")))
    i += 1
ln = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < n:
    if l[i] == 1:
        ln[0] += 1
    if l[i] == 2:
        ln[1] += 1
    if l[i] == 3:
        ln[2] += 1
    if l[i] == 4:
        ln[3] += 1
    if l[i] == 5:
        ln[4] += 1
    if l[i] == 6:
        ln[5] += 1
    if l[i] == 7:
        ln[6] += 1
    if l[i] == 8:
        ln[7] += 1
    if l[i] == 9:
        ln[8] += 1
    if l[i] == 10:
        ln[9] += 1
    i += 1


if ln[0] > ln[1] and ln[0] > ln[2] and ln[0] > ln[3] and ln[0] > ln[4] and ln[0] > ln[5] and ln[0] > ln[6] and ln[0] > ln[7] and ln[0] > ln[8] and ln[0] >ln[9]:
    if ln[0] > n/2:
        print("the 1th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[1] > ln[0] and ln[1] > ln[2] and ln[1] > ln[3] and ln[1] > ln[4] and ln[1] > ln[5] and ln[1] > ln[6] and ln[1] > ln[7] and ln[1] > ln[8] and ln[1] >ln[9]:
    if ln[1] > n/2:
        print("the 2th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[2] > ln[0] and ln[2] > ln[1] and ln[2] > ln[3] and ln[2] > ln[4] and ln[2] > ln[5] and ln[2] > ln[6] and ln[2] > ln[7] and ln[2] > ln[8] and ln[2] >ln[9]:
    if ln[2] > n/2:
        print("the 3th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[3] > ln[1] and ln[3] > ln[2] and ln[3] > ln[0] and ln[3] > ln[4] and ln[3] > ln[5] and ln[3] > ln[6] and ln[3] > ln[7] and ln[3] > ln[8] and ln[3] >ln[9]:
    if ln[3] > n/2:
        print("the 4th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[4] > ln[1] and ln[4] > ln[2] and ln[4] > ln[3] and ln[4] > ln[0] and ln[4] > ln[5] and ln[4] > ln[6] and ln[4] > ln[7] and ln[4] > ln[8] and ln[4] >ln[9]:
    if ln[4] > n/2:
        print("the 5th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[5] > ln[1] and ln[5] > ln[2] and ln[5] > ln[3] and ln[5] > ln[4] and ln[5] > ln[0] and ln[5] > ln[6] and ln[5] > ln[7] and ln[5] > ln[8] and ln[5] >ln[9]:
    if ln[5] > n/2:
        print("the 6th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[6] > ln[1] and ln[6] > ln[2] and ln[6] > ln[3] and ln[6] > ln[4] and ln[6] > ln[5] and ln[6] > ln[0] and ln[6] > ln[7] and ln[6] > ln[8] and ln[6] >ln[9]:
    if ln[6] > n/2:
        print("the 7th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[7] > ln[1] and ln[7] > ln[2] and ln[7] > ln[3] and ln[7] > ln[4] and ln[7] > ln[5] and ln[7] > ln[6] and ln[7] > ln[0] and ln[7] > ln[8] and ln[7] >ln[9]:
    if ln[7] > n/2:
        print("the 8th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[8] > ln[1] and ln[8] > ln[2] and ln[8] > ln[3] and ln[8] > ln[4] and ln[8] > ln[5] and ln[8] > ln[6] and ln[8] > ln[7] and ln[8] > ln[0] and ln[8] >ln[9]:
    if ln[8] > n/2:
        print("the 9th cheese party won")
    else:
        print("no cheese party has the majority")
if ln[9] > ln[1] and ln[9] > ln[2] and ln[9] > ln[3] and ln[9] > ln[4] and ln[9] > ln[5] and ln[9] > ln[6] and ln[9] > ln[7] and ln[9] > ln[8] and ln[9] >ln[0]:
    if ln[9] > n/2:
        print("the 10th cheese party won")
    else:
        print("no cheese party has the majority")




print(l, "\n", ln)
