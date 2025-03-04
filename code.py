def find_Max_Num(num_list):
    max_num = ''
    for i in range(len(num_list),0,-1):
        max_num = max_num + str(num_list[i-1])
    return int(max_num)
