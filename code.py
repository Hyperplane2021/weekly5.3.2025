def find_Max_Num(lst):
    return int("".join(map(str, sorted(lst, reverse=True))))
