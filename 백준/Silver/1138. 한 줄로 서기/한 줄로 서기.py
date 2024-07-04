r=[];n=int(input())
for q in input().split()[::-1]:r.insert(int(q),n);n-=1
print(*r)