# from collections import deque

# def solution(queue1, queue2):
#     answer = 0
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     s1 = sum(q1)
#     s2 = sum(q2)
    
#     # 두 큐의 합이 짝수여야만 수행 가능
#     sum_q = sum(q1+q2)
#     if sum_q % 2 != 0:
#         return -1
    
#     # 다시 제자리로 돌아올 때까지 무한반복
#     while answer < len(queue1) * 4:
#         if s1 > s2:
#             q2.append(q1.popleft())
#             answer += 1
#             s1 -= q2[-1]
#             s2 += q2[-1]
#         elif sum(q1) < sum(q2):
#             q1.append(q2.popleft())
#             answer += 1
#             s1 += q1[-1]
#             s2 -= q1[-1]
#         else: # 두 큐의 합이 같아졌을 때
#             break
#         if answer == len(queue1) * 4:
#             return -1
#             break
#     return answer

from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1
        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer