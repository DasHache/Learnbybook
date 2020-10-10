# To run this file
# python3 ./bamboo.py "1 2 10 3"
# ... 
# Answer = 4


def splitter(a, m): 
    ''' 
    Input: 
      a = list of integers, example: [1, 2, 3, 4]
      m = element to split the list, example: 3
    Output: 
      list of lists of integers, example: [ [1, 2], [4] ]
    '''
    # make list of strings from list of int
    list_of_str = [str(i) for i in a] 
    # make string "1 2 3 4" from list ["1","2","3","4"]
    s = ' '.join(list_of_str) 
    # if m = 3, make ["1 2 ", " 4"] from "1 2 3 4"
    list_of_str = s.split(str(m)) 
    # make [ ["1", "2"], ["4"] ] from ["1 2 ", " 4"]
    list_of_lists_of_str = [a_string.split() for a_string in list_of_str] 
    # make [ [1, 2], [4] ] from [ ["1", "2"], ["4"] ]
    list_of_lists_of_int = [ [int(si) for si in s] for s in list_of_lists_of_str] 
    return list_of_lists_of_int

def sword_stroke(a):
    '''
    Input: 
      a = list of integers
    Output: 
      sum_len = number of sword strokes required 
    '''
    print("Input list: ", str(a))

    # CHECK: 'a' must be a list
    if not isinstance(a, list): raise TypeError 
    if len(a) == 0: 
        return 0 # Empty list => zero stroke

    # CHECK: 'a' must be a list of integers
    if not isinstance(a[0], int): raise TypeError 
    if len(a) == 1: 
        return 1 # Single element => 1 stroke

    # find the maximum element and split the array
    m = max(a)
    list_of_lists = splitter(a, m)
    sum_len = 1

    # summ up (recursively) for all the splits
    for an_list in list_of_lists:
        list_len = sword_stroke(an_list) 
        sum_len = sum_len + list_len 

    print("<== ", str(sum_len))
    return sum_len 


# Entry point
from sys import argv
str_of_int = argv[1] # second command line argument: string of integers
list_of_int = [int(s) for s in str_of_int.split()] # make it a list of integers

answer = sword_stroke(list_of_int) 
print("Answer =", answer)


# Examples of "splitter" function calls:
 
# >>> splitter([4,4,4,3], 4)
# [[], [], [], ['3']]
# >>> splitter([4,4,4,3,4], 4)
# [[], [], [], ['3'], []]
# >>> splitter([4,4,4,3,2,1,3,4], 4)
# [[], [], [], ['3', '2', '1', '3'], []]
# >>> splitter([4,5,4,4,3,2,1,3,4], 4)
# [[], ['5'], [], ['3', '2', '1', '3'], []]



# function: sword_stroke
# input: list of numbers
# logic: 
# - find the max element(s) 
# - split the list into several lists (without the max element)
# - call sword_stroke on all the list and summ up the return values
# return = possible cases: 
# - case1: len 0: []
#        : then return 0
# - case2: all are equal: [4,4,4]
#        : then return 1
# - case3: not all are equal: [4,4,4,3] or [4,4,3,4] or [4,1,2,1,3]
#        : then split by the max number and call sword_stroke again on each part:
#        : examples: 
#          [4,4,4,3] => [], [], [], [3]       => 0 + 0 + 0 + 1
#          [4,4,3,4] => [], [], [3], []       => 0 + 0 + 1 + 0
#          [4,1,2,1,4,3] => [], [1,2,1], [3]  => 0 + x + 1, where x = sword_stroke([1,2,1])
