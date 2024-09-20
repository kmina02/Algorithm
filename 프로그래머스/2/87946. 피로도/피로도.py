from itertools import permutations
def solution(k, dungeons):
    answer = -1
    sort_list = permutations(dungeons)
    for s in sort_list:
        ss = list(s)
        a, new_k = 0, k
        for i in range(len(dungeons)):
            if new_k >= ss[i][0]:
                a += 1
                # print(ss, "인 경우에", a, "개의 던전 통과")
                answer = max(answer, a)
                new_k -= ss[i][1]
            else:
                break
                
    return answer