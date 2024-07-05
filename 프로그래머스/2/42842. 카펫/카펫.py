def solution(brown, yellow):
    s = int((brown - 4) / 2)
    for i in range(1, s):
        print(i)
        if i * (s - i) == yellow:
            return sorted([i+2, s-i+2], reverse = True)