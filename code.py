def find_Max_Num(lst):
    max_num = ''
    lst = sorted(lst, reverse=True)
    for num in lst:
        max_num += str(num)
    
    return int(max_num)


###
This function takes a list of numbers as input, 
sorts them in descending order, 
and then converts the list into a string. 
It then converts this string back into an integer. 
This effectively returns the largest number in the list.
###

