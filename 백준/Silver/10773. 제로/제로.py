k = int(input())
money = []
for _ in range(k):
    m = int(input())
    if m == 0:
        money.pop()
    else:
        money.append(m)
print(sum(money))