from collections import deque
def solution(priorities, location):
    execute = []
    num = deque(list(range(len(priorities))))
    priorities = deque(priorities)    
    # priorities가 텅 빈 큐가 될 때까지 무한반복
    while len(priorities) > 0:
        # priorities에서 맨 앞 원소를 꺼내서 p 변수에 넣고, num에서 맨 앞 원소를 꺼내서 n 변수에 넣기
        p = priorities.popleft()
        n = num.popleft() 
        # priorities 원소의 최댓값이 p보다 크다면 p를 다시 큐에 넣고 n도 다시 큐에 넣기
        if priorities == deque():
            execute.append(n)
            print(f"우선순위가 {p}인 프로세스 {n}를 실행한다.")
            break
        if max(priorities) > p:
            priorities.append(p)
            num.append(n)
            print(f"우선순위가 {p}인 프로세스 {n}를 다시 큐에 넣는다.")
        # 그렇지 않다면 n을 execute 리스트에 append하기
        else:
            execute.append(n)
            print(f"우선순위가 {p}인 프로세스 {n}를 실행한다.")
    # execute[location]을 반환
    return execute.index(location) + 1