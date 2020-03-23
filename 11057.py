# 오르막 수 # dp

# 범위 1자리부터 1000자리.
# 그리디 불가

n = int(input())

dp = [[0] * 10 for i in range(1002)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] = (dp[i][j] + dp[i - 1][k]) % 10007

ans = 0
for i in range(10):
    ans = (ans + dp[n][i]) % 10007

print(ans)