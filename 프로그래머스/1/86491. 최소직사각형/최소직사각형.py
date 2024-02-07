def solution(sizes):
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
    w = [i[0] for i in sizes]
    h = [j[1] for j in sizes]
    return max(w) * max(h)