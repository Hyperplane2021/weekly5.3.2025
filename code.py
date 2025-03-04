def find_Max_Num(nums):
    max_num = 0
    for i in str(nums):
        for j in str(nums):
            if i!=j and int(str(nums).replace(i,'')) > int(str(nums).replace(j,'')):
                return int(i+j+str(nums).replace(i,'').replace(j,''))
    return max_num
