def find_Max_Num(num_list):
    num_list.sort(reverse=True)
    max_num = int(''.join(map(str, num_list)))
    return max_num
