def rabbit_count(n,k):
    a, b = 1,1
    for i in range(n-2):
        a,b = b, b+k*a
    return b

print(rabbit_count(31,3))
