H, W = map(int, input().split())
cloud = []
for i in range(1, H+1): #i=1,2,...,H
  s = input()
  for j in range(1, W+1):
    if j==1 and s[j-1]=='.':
      cloud.append(-1)
    if s[j-1]=='c':
      cloud.append(0)
    else:
      for k in range(j-1, 0, -1):
        if s[k-1]=='c':
          cloud.append(j-k)
          break
        if s[:j]=='.'*j:
          cloud.append(-1)
          break
          
for t in range(H*W):
  if (t+1)%W==0: print(cloud[t], end='\n')
  else: print(cloud[t], end=' ')