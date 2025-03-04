def find_Max_Num(digits):
    digits.sort()
    max_num = ''
    while digits:
        while digits[0] == 0:
            digits.pop(0)
        if not digits:
            break
        max_num += str(digits.pop(0))
    return int(max_num)
