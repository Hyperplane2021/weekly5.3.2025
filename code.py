def find_Max_Num(lst):
    max_num = ''
    max_num_str = ''
    for i in sorted(lst, reverse=True):
        max_num += str(i)
    for i in range(len(max_num)):
        max_num_str += max_num[i]
        if i % 2 != 0:
            max_num_str += max_num[len(max_num) - i - 1]
    # max_num_str = str(max_num)[::-1]
    return int(max_num_str)

###
This function takes a list of numbers as input, 
sorts them in descending order, 
and then constructs a new string by alternating between the largest and second largest numbers. 
The function then converts this string back into an integer and returns it.
###
