def find_Max_Num(digits):
    from itertools import permutations
    digits = set(digits)
    max_num = 0
    for p in permutations(digits):
        num = int(''.join(map(str, p)))
        if num > max_num:
            max_num = num
    return max_num
