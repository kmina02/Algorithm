n = int(input())
height = [0] + list(map(int, input().split()))
answer = []

for k in range(n, 0, -1): 
    target = k
    info = height[k]
    count = 0
    if info == 0:
        answer.insert(0, target)
    else:
        for i in range(len(answer)):
            if answer[i] > target: 
                count += 1
            if count == info:
                answer.insert(i+1, target)
                break
print(' '.join([str(a) for a in answer]))