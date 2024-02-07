def solution(answers):
    answer = []
    s = [0, 0, 0, 0]
    st1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    st2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    for i in range(len(answers)): # 0~4
        if answers[i] == st1[i]:
            s[1] += 1
        if answers[i] == st2[i]:
            s[2] += 1
        if answers[i] == st3[i]:
            s[3] += 1

    m = max(s)
    
    for j in range(len(s)):
        if s[j] == m:
            answer.append(j)
    return answer