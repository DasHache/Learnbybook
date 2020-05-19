from math import factorial
import numpy as np
n = 12
m = 3
b = 3
t = np.array(range(pow(b,m)))

def f(i):
    return np.base_repr(i, b, padding=10)[-b:]

vf = np.vectorize(f)
tb = vf(t)

def right(x):
    if x[0] == x[1] == x[2]:
        return False
    if x[0:2] == "01" or x[0:2] == "12" or x[0:2] == "20":
        return True
    if x[0] == x[1]:
        if x[1:] == "01" or x[1:] == "12" or x[1:] == "20":
            return True

tb_right = [x for x in tb if right(x)]

def get_left_from_right():
    left = []
    for i in range(len(tb_right)):
        t_left = str(222 - int(tb_right[i]))
        left.append(("0000"+t_left)[-3:])
    return left

tb_left = get_left_from_right()

tb_i0 = [[x for x in tb_right if x[0] == str(y)] for y in range(m)]
tb_i1 = [[x for x in tb_right if x[1] == str(y)] for y in range(m)]
tb_i2 = [[x for x in tb_right if x[2] == str(y)] for y in range(m)]

def base3(y):
    return [tb_right.index(x) for x in y]

print('Problem:\nYou have 12 coins that all look exactly the same. \
One might be counterfeit and it is either heavier or lighter than the other 11. \
With a balance beam scale, isolate the counterfeit coin in three moves.')

print('Enter the result of a measurement as:\n\t0 if left is heavier,\n\t1 if equal or\n\t2 if right is heavier\n')
print('Please put coins {} on the left and coins {} on the right'.format(base3(tb_i0[0]), base3(tb_i0[2])))
i0_res = input('Enter the result: ')

print('Please put coins {} on the left and coins {} on the right'.format(base3(tb_i1[0]), base3(tb_i1[2])))
i1_res = input('Enter the result: ')

print('Please put coins {} on the left and coins {} on the right'.format(base3(tb_i2[0]), base3(tb_i2[2])))
i2_res = input('Enter the result: ')

i_res = i0_res+i1_res+i2_res
if i_res in tb_right:
    print('The answer: coin {} is heavier.'.format(tb_right.index(i_res)))
elif i_res in tb_left:
    print('The answer: coin {} is lighter.'.format(tb_left.index(i_res)))
else:
    print('The answer: all coins have the same weight.')
