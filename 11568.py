# 민균이의 계략 # dp

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

maxNum = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    if maxNum < dp[i]:
        maxNum = dp[i]
print(maxNum)

