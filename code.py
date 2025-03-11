def find_Max_Num(lst):
    return int("".join(map(str, sorted(lst, reverse=True))))

###
This function takes a list of numbers as input, 
sorts them in descending order, 
converts them to strings, 
joins them together, 
and then converts the result back to an integer. 
It returns this integer.
###
