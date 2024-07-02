from itertools import permutations

def solution(numbers):
    # numbers를 리스트로 만든다.
    num_list = [i for i in numbers] 
    
    # 만들 수 있는 모든 경우의 수를 만든다.
    can_list = []
    for n in range(1, len(num_list) + 1):
        for c in permutations(num_list, n):
            can_list.append(int(''.join(c))) 
    # 중복을 제거한다.
    can_list = sorted(list(set(can_list)))
    print(can_list)
    if 0 in can_list:
        can_list.remove(0)
    if 1 in can_list:
        can_list.remove(1)
    # 소수 여부를 확인한다.      
    for c in can_list[:]:
        for i in range(2, c):
            if c % i == 0:
                can_list.remove(c)
                break
    return len(can_list)