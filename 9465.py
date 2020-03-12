# 스티커 # DP
import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    ans = 0
    n = int(input().strip())
    a = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]
    dp[0][1] = a[0][1] + a[1][0]  # 현재꺼 + 이전 대각선꺼
    dp[1][1] = a[1][1] + a[0][0]
    for i in range(2, n):
        dp[0][i] = a[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = a[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))
