n = int(input())
table = [0] * (n + 1)

cnt1 = 0
cnt2 = 0

def fib(n):
    global cnt1

    if (n == 1 or n == 2):
        cnt1 += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global cnt2

    table[1] = 1
    table[2] = 1

    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        cnt2 += 1

    return table[n]
    
fib(n)
fibonacci(n)

print(cnt1, end = ' ')
print(cnt2)