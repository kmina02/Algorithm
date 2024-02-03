def solution(n, lost, reserve):
    cloth = [1] * (n + 1)
    for l in lost:
        cloth[l] -= 1
    for r in reserve:
        cloth[r] += 1
    for c in range(1, len(cloth)):
       if cloth[c:c+2] == [0, 2]:
            cloth[c:c+2] = [1, 1]
       elif cloth[c:c+2] == [2, 0]:
            cloth[c:c+2] = [1, 1]

    cloth = [x for x in cloth if x != 0]
    return len(cloth)-1