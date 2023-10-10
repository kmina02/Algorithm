N = int(input())
switch = [-1] + list(map(int, input().split())) # 스위치 번호와 인덱싱 맞추기 위해 앞에 -1 추가

# 학생수 입력
std = int(input())

for i in range(std):
  # 성별, 숫자 받기
  sex, n =map(int, input().split())
  # 남학생의 경우
  if sex==1:
    for i in range(n, N+1, n):
      switch[i] = abs(switch[i]-1)
  # 여학생의 경우
  else:
    switch[n] = abs(switch[n]-1)
    for i in range(N//2):
      l, r=(n-i), (n+i)
      if l<1 or r>N: break # 스위치 범위를 벗어나면 break
      if switch[l]==switch[r]: # 스위치 상태가 동일하면 더 양옆으로 나가기
        switch[l] = abs(switch[l]-1)
        switch[r] = abs(switch[r]-1)
      else: break
# 출력값 출력
for i in range(1, N+1):
  if i%20==0:
    print(switch[i])
  else: 
    print(switch[i], end=' ')