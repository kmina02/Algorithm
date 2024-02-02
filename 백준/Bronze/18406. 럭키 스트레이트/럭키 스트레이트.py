n = input()
left, right = 0, 0
for l in n[:len(n)//2]:
  left += int(l)
for r in n[len(n)//2:]:
  right += int(r)

if left == right:
  print("LUCKY")
else:
  print("READY")