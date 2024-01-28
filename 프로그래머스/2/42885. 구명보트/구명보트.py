def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people)-1
    
    while end - start >= 1:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer + (end - start + 1)