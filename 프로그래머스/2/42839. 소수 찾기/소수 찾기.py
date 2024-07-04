from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    # numbers를 리스트로 만든다.
    num_list = list(numbers)
    
    # 만들 수 있는 모든 경우의 수를 만든다.
    can_list = set()
    for i in range(1, len(num_list) + 1):
        can_list.update(int(''.join(c)) for c in permutations(num_list, i))

    # 소수 여부를 확인한다.
    answer = sum(1 for c in can_list if is_prime(c))
            
    return answer