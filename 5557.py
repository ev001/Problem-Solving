# 조합론 # 1학년

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

# dp 배열의 인덱스 = 이전의 값을 계산한 현재의 결과값 +

dp[0][arr[0]] = 1
for i in range(1, n):
    for j in range(21):
        if dp[i - 1][j]:
            minus = j - arr[i]
            plus = j + arr[i]
            if minus >= 0:
                dp[i][minus] += dp[i - 1][j]
            if 20 >= plus:
                dp[i][plus] += dp[i - 1][j]

print(dp)
print(dp[n-2][arr[-1]])
