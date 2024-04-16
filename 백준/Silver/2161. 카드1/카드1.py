# 2161
n = int(input())
card = [i for i in range(1, n+1)]
answer = []
while card != []:
    answer.append(card.pop(0))
    if card != []:
        card.append(card.pop(0))
for a in answer:
    print(a, end = ' ')