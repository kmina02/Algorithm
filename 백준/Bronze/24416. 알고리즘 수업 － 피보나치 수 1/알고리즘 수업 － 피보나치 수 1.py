n = int(input())
count_recur, count_dp = 0, 0
f = [0] * (n+1)

def fib_recur(n):
  global count_recur 
  if (n==1 or n==2):
    count_recur += 1
    return 1
  else:
    return fib_recur(n-1) + fib_recur(n-2)

def fib_dp(n):
    global count_dp
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        count_dp += 1
        f[i] = f[i-1] + f[i-2]
    return f[i]

fib_recur(n)
fib_dp(n)
print(count_recur, count_dp)