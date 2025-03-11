def find_Max_Num(digits):
    max_number = [str(x) for x in sorted(digits, reverse=True)]
    return int(''.join(max_number))

###
This function takes a list of digits as input 
and returns the largest number that can be formed by rearranging these digits. 
It does this by first converting each digit to a string, 
sorting the strings in descending order, 
and then joining them back together into a single string. 
The resulting string is then converted back to an integer and returned.
###