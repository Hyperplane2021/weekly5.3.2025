def find_Max_Num(lst):
    lst = sorted(list(set(lst)), reverse=True)
    return int(''.join(map(str, lst)))
