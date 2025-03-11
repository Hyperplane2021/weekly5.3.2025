def find_Max_Num(nums):
    max_num = 0
    for i in str(nums):
        for j in str(nums):
            if i!=j and int(str(nums).replace(i,'')) > int(str(nums).replace(j,'')):
                return int(i+j+str(nums).replace(i,'').replace(j,''))
    return max_num

###
This function takes a single number as input 
and returns the sum of the two digits that are not equal to each other. 
If no such pair of digits exists, 
it returns the maximum digit in the number.
###
