# 이친수 # DP

n = int(input())

dp = [[0, 0] for _ in range(93)]

# 순서 [0일때, 1일때]
dp[1] = [0, 1]
dp[2] = [0, 1]
dp[3] = [1, 1]

for i in range(4, n + 1):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n]))

'''
    어렴풋이 이해했을 때 바로 코드 작성하지말고
    완벽히 분석하고 코드로 옮기기.
    
    dp[n] = ~ 으로 작성해놓은 코드를
    실제 for 문 돌때 n을 i 로 바꾸는거 잊지말기.
'''
