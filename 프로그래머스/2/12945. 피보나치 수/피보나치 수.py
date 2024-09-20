def solution(n):
    a, b = 0, 1
    if n == 0: return 0
    elif n == 1: return 1
    else:
        for i in range(2, n+1):
            c = (a + b) % 1234567
            if i % 2 == 0: a = c
            else: b = c 
        return c % 1234567