def list_sum(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + list_sum(a_list[1:])
print(list_sum([1,2,3,4]))