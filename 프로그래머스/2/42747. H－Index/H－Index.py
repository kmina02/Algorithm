def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations)):  
        if i+1 > citations[i]:
            return i
    return len(citations)
        
        
        # 6 5 3 1 0
        # 8 8 4 3 2 1
        # i = 0 1 2 3 4