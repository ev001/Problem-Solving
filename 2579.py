import sys

input = sys.stdin.readline

n = int(input())
a = [int(input().strip()) for _ in range(n)]
dp = [0] * n

if n >= 1:
    dp[0] = a[0]  # 첫번째 계단
if n >= 2:
    dp[1] = a[1] + dp[0]  # 두번째 계단
if n >= 3:
    dp[2] = max(dp[0] + a[2], a[1] + a[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + a[i], a[i] + a[i - 1] + dp[i - 3])

print(dp[- 1])

'''
    계단이 3개 이하일때의 예외 case 추가
'''