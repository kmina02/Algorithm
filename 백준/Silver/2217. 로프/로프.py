n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()

answer = 0
for i in range(n):
    if answer < rope[i] * (n-i):
        answer = rope[i] * (n-i)
print(answer)