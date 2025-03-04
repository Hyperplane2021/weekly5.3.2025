def find_Max_Num(digits):
    max_number = [str(x) for x in sorted(digits, reverse=True)]
    return int(''.join(max_number))
