from itertools import permutations
def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    # numbers를 리스트로 만든다.
    num_list = list(numbers)
    
    # 만들 수 있는 모든 경우의 수를 만든다.
    can_list = []
    for i in range(1, len(num_list) + 1):
        can_list += list(permutations(num_list, i))
    can_list = [int(''.join(c)) for c in can_list]
    # 중복을 제거한다.
    can_list = sorted(list(set(can_list)))

    # 소수 여부를 확인한다.      
    for c in can_list:
        if c <= 1:
            continue
        elif is_prime(c):
            answer += 1
            
    return answer