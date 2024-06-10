k = int(input())
colored_paper = []

for _ in range(k):
  a = list(map(int, input().split()))
  colored_paper.append(a)

white = 0
blue = 0

def devide(x, y, n):
    global white, blue
    color = colored_paper[x][y] 

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != colored_paper[i][j]:
                devide(x, y, n // 2)                      
                devide(x, y + n // 2, n // 2)             
                devide(x + n // 2, y, n // 2)             
                devide(x + n // 2, y + n // 2, n // 2)    
                return

    if color == 0:
        white += 1
    else:
        blue += 1

devide(0, 0, k)
print(white, blue, sep='\n')