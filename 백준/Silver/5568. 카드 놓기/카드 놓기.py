import sys
from itertools import permutations
n = int(input())
k = int(input())
card = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set("".join(c) for c in permutations(card, k))))