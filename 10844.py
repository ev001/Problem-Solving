# 쉬운 계단수 # DP

import sys

input = sys.stdin.readline

mod = 1000000000
n = int(input().strip())
dp = [[0] * 10 for _ in range(101)]

# n이 1일때 1~9의 dp값은 1
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):  # 10 11
        if j == 0:  # + 경우만 있음.
            dp[i][0] = dp[i - 1][1] % mod
        elif j == 9:
            dp[i][9] = dp[i - 1][8] % mod
        else:
            dp[i][j] = (dp[i - 1][j + 1] + dp[i - 1][j - 1]) % mod

sum = 0
for i in range(1,10):
    sum += dp[n][i]

print(sum % mod)

'''
사고의 흐름

n : 1
1 2 3 4 5 6 7 8 9 -> 9

n: 2
12
21 23
32 34
43 44
54 56
65 66
...     -> 16
n:3
123 121
212 232 234

즉 , 앞의 수에서 +1 -1 케이스 모두 꺼내기
저장을 어떤식으로 ?
'''