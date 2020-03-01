import sys

input = sys.stdin.readline

n = int(input())
a = [int(input().strip()) for _ in range(n)]
dp = [0]*n

dp[0] = a[0]                            # 첫번째 계단
dp[1] = a[1] + dp[0]                    # 두번째 계단
dp[2] = max(dp[0] + a[2], a[1] + a[2])  # 세번째 계단

for i in range(3, n):
    dp[i] = max(dp[i - 2] + a[i], a[i] + a[i - 1] + dp[i - 3])

print(dp[n-1])
