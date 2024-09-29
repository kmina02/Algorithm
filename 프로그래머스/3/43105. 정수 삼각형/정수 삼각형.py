def solution(triangle):
    # def dp(x, y):
    #     if x < len(triangle) - 1:
    #         triangle[x][y] += max(dp(x+1, y), dp(x+1, y+1))
    #     print(x, y, triangle[x][y])
    #     return triangle[x][y]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]