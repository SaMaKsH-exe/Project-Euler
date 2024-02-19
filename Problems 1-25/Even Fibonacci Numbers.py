
def fibonacci(n):
    a = 1
    b = 2
    sum = 0
    while b < n:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum

print(fibonacci(4000000))