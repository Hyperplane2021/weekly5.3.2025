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

###
This function takes a list of digits as input 
and returns the largest number that can be formed by rearranging these digits. 
It does this by sorting the digits 
and then constructing the largest possible number from the sorted digits.
###
