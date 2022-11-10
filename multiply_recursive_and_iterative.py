def multiply_iterative(n, a):
    res = 0
    for i in range(a):
        res += n
    return res 
print(multiply_iterative(3, 4))

def multiply_recursive(n, a):
    if a == 0:
        return 0 
    return n + multiply_recursive(n, a-1)
print(multiply_recursive(3, 4))