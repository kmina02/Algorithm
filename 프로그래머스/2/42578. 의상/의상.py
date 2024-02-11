def solution(clothes):
    closet = {}
    answer = 1
    for i in clothes:
        if i[1] in closet:
            closet[i[1]].append(i[0])
        else:
            closet[i[1]] = [i[0]]
    for c in closet:
        answer *= ( len(closet[c]) + 1)
        print(answer)
    return answer - 1
    