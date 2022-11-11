def str_len_iterative(a_str):
    res = 0
    while a_str:
        res += 1
        a_str = a_str[1:]
    return res
print(str_len_iterative("abc"))


def str_len_recursive(a_str):
    if not a_str:
        return 0 
    return 1 + str_len_recursive(a_str[1:])
print(str_len_recursive("abcdefghijklmnopqrstuvwxyz"))