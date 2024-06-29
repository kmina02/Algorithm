from itertools import combinations

def solution(number, k):
    n = len(number)
    for _ in range(k):
        max_list = []
        for i in range(n): # i = 0, 1, 2
            max_list.append(int(number[:i] + number[i+1:]))
            print(max_list)
        number = str(max(max_list))
        n -= 1
    return number
        
        
    
            