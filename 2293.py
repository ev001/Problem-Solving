import sys
from itertools import combinations

input = sys.stdin.readline

# 동전 1 # dp

n, k = map(int, input().split())
arr = [int(input().strip()) for _ in range(n)]

dp = [0] * 10001
dp[0] = 1
for i in arr:
    for j in range(i, k + 1):
        dp[j] += dp[j-i]
print(dp[k])

'''
    핵심 
    목표금액 - 사용하는 동전의 값 >= 0
'''