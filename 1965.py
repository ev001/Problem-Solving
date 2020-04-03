# 상자넣기 # dp

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
ans = 0
for i in range(n):
    for j in range(0, i):
        if a[j] < a[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
    if dp[i] > ans:
        ans = dp[i]
print(ans)

# 예전에 풀었던 최장 증가수열이 생각나서 그 방식으로 풀었음.
