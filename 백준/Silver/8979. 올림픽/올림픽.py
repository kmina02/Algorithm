E, C = map(int, input().split())
score=[0]*E
medal=[1]*E
for i in range(E):
  s = input()
  country = int(s[0])
  score[country-1] = int(s[2])*100+int(s[4])*10+int(s[6])*1

for i in range(E):
  for j in range(E):
    if score[i]<score[j]:
      medal[i]+=1

print(medal[C-1])