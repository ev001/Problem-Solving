n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

'''
1; n == 0 인경우
2; m == 0 인경우 
3; 그외
'''
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            pass
        if i == 0 and j - 1 >= 0:
            dp[i][j] = dp[i][j - 1] + a[i][j]
        elif j == 0 and i - 1 >= 0:
            dp[i][j] = dp[i - 1][j] + a[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + a[i][j]
print(dp[n - 1][m - 1])
