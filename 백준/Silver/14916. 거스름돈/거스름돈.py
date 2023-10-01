n = int(input())
c5 = n // 5
a = n % 5

if a == 0:
    c2 = 0
elif a == 2:
    c2 = 1
elif a == 4:
    c2 = 2
else:
    if c5 > 0:
        c5 -= 1
        a += 5
        c2 = a // 2
    else:
        print(-1)
        exit()

answer = c5 + c2
print(answer)