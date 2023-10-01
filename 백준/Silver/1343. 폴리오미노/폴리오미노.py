a = input()
answer = ''
i = 0
while i<len(a):
  if a[i:i+4]=='XXXX':
    answer += 'AAAA'
    i += 4
  elif a[i:i+2]=='XX':
    answer += 'BB'
    i += 2
  else:
    answer += a[i]
    i += 1

print(answer if 'X' not in answer else -1)