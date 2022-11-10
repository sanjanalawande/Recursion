def exponential_iterative(n, a):
    res = 1
    for i in range(a):
        res = res * n 
    return res 
print(exponential_iterative(3, 3))

def exponential_recursive(n, a):
    if a == 1:
        return n 
    return n * exponential_recursive(n, a-1)
print(exponential_recursive(3, 4))