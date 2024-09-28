def solution(operations):
    answer = []
    for o in operations:
        if o[0] == "I":
            answer.append(int(o[2:]))
        elif o == "D 1":
            answer = answer[:-1]
        else:
            answer = answer[1:]
        answer.sort()
    if answer == []:
        return [0, 0]
    else:
        return [answer[-1], answer[0]]
