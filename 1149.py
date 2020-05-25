# RGB거리 #DP

import sys

input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for i in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = arr[i - 1][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = arr[i - 1][1] + min(dp[i - 1][2], dp[i - 1][0])
    dp[i][2] = arr[i - 1][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n]))

'''
선택할 수 있는 경우의 수는 3가지 R G B

쭉 나열해보자.

dp[1][0] = 26
dp[1][1] = 40
dp[1][2] = 83

dp[2][0] = 49 + (40 || 83)
dp[2][1] = 60 + (26 || 83)
dp[2][2] = 57 + (26 || 40)    

... 규칙발견!

'''
