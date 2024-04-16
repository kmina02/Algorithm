# 10799
lazer = input()
i, answer = 0, 0
stack = []
while i < len(lazer):
  if lazer[i] == "(":
    if lazer[i+1] == ")":
        answer += len(stack)
        i += 1
    else:
        stack.append(lazer[i])
  else:
    stack.pop()
    answer += 1
  i += 1
print(answer)