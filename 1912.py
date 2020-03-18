# 연속합 # DP # 3/17 22:08 start 22:20 end

import sys

input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))
dp = [0 for i in range(N)]
dp[0] = a[0]
for n in range(1, N):
    dp[n] = max(a[n] + dp[n - 1], a[n])

print(max(dp))
