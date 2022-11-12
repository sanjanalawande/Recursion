import time
def fibonacci_memoization(n, cache= None):
    if cache == None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n 
    result = fibonacci_memoization(n-1, cache) + fibonacci_memoization(n-2, cache)
    cache[n] = result 
    return result 


n = 900
start = time.perf_counter()
fibonacci_memoization(n)
end = time.perf_counter()
print("Manual cache version. Seconds taken = {:.7f}".format(end - start))

