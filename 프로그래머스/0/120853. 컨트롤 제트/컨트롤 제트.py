def solution(s):
    answer = 0
    ss = s.split(" ")[::-1]
    for i in range(len(ss)):
        if ss[i] == "Z":
            answer -= int(ss[i+1])
        else:
            answer += int(ss[i])
    return answer