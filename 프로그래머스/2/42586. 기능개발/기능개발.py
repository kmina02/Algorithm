from collections import deque

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        p, s = progresses[i], speeds[i]
        if (100 - p) % s == 0:
            days.append((100 - p) // s)
        else:
            days.append((100 - p) // s + 1)
            
    answer = []     
    today = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] > today:
            answer.append(count)
            today = days[i]
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer
        
    
        
    