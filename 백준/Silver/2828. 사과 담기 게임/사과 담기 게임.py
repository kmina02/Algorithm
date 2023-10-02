N, M = map(int, input().split())
a = int(input())
s=1
answer=0
for k in range(a):
  i = int(input())
  if s<=i<(s+M): l=0
  elif i<s: l=i-s
  else:l=i-s-M+1 
  s+=l
  answer+=abs(l)
print(answer)