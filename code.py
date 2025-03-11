def find_Max_Num(lst):
    lst = sorted(list(set(lst)), reverse=True)
    return int(''.join(map(str, lst)))

###
This function takes a list of numbers as input, 
sorts them in descending order, 
removes duplicates by converting the list to a set and then back to a list, 
and then converts the list back to a string. 
The string is then converted to an integer and returned.
###
