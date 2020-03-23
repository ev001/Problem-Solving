# 가장 큰 증가 부분 수열

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
max = 0

for i in range(n):
    maxDp = 0
    for j in range(i):
        if arr[j] < arr[i]:
            if maxDp < dp[j]:
                maxDp = dp[j]
    dp[i] = maxDp + arr[i]
    if max < dp[i]:
        max = dp[i]

print(max)
