def find_Max_Num(digits):
    from itertools import permutations
    digits = set(digits)
    max_num = 0
    for p in permutations(digits):
        num = int(''.join(map(str, p)))
        if num > max_num:
            max_num = num
    return max_num

###
This function takes a list of digits 
and returns the largest number that can be formed using these digits. 
It does this by generating all possible permutations of the digits, 
converting each permutation to an integer, 
and keeping track of the largest number found.
###

