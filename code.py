def find_Max_Num(num_list):
    num_list.sort(reverse=True)
    max_num = int(''.join(map(str, num_list)))
    return max_num

###
This function takes a list of numbers as input, 
sorts them in descending order, 
and then converts them into a single integer. 
It returns this integer.
###
