n = int(input())

# 테이블화
table = [[0] * (n+1) for _ in range(n+1)]

# 테이블 채워넣기
for i in range(1, n+1):
    table[i][1:i+1] = list(map(int, input().split()))

# 최대값 채워넣기
for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        table[i][j] += max(table[i+1][j], table[i+1][j+1])

print(table[1][1])