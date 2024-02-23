def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        result = sorted(array[i-1:j])[k-1]
        answer.append(result)
    return answer