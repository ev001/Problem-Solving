# 1로 만들기 # dp

n = int(input())

dp = [0] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        temp = dp[i]
        dp[i] = dp[i // 2] + 1
        if temp < dp[i]:
            dp[i] = temp

    if i % 3 == 0:
        temp = dp[i]
        dp[i] = dp[i // 3] + 1
        if temp < dp[i]:
            dp[i] = temp

print(dp[n])

'''
    3가지 case를 모두 해보고
    최소의 횟수를 bottom up 으로 판단 후
    dp에 저장
'''