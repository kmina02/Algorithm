import datetime
# 입력, 변수 설정
N = int(input())
score = []
times = [0]
t1, t2 = 0, 0
s1, s2 = 0, 0

# 시간(문자열)을 분으로 바꿔주는 함수
def minute(x):
  m, s = map(int, x.split(':'))
  x = m*60 + s
  return(x)

# 분을 시간(문자열)로 바꿔주는 함수
def time(x):
  m = x // 60
  s = x % 60
  print("{:02d}:{:02d}".format(m, s))

# 반복문으로 정보 입력
for i in range(N):
  n, t = input().split()
  if n=='1': s1+=1
  else: s2+=1
  times.append(minute(t))
  score.append([s1, s2])
times.append(2880)

# 반복문으로 시간 계산
for j in range(N):
  if score[j][0]>score[j][1]:
    t1+=(times[j+2] - times[j+1])
  elif score[j][0]<score[j][1]:
    t2+=(times[j+2] - times[j+1])
  else: continue

# 출력
time(t1)
time(t2)
