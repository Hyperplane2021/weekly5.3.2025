def find_Max_Num(lst):
    max_num = ''
    lst = sorted(lst, reverse=True)
    for num in lst:
        max_num += str(num)
    
    return int(max_num)
