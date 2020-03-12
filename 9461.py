# 파도반 수열 # dp

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
tc = int(input().strip())

for i in range(tc):
    a = int(input().strip())
    if a > 4:
        for j in range(4, a + 1):
            dp[j] = dp[j - 2] + dp[j - 3]
    print(dp[a])

''' 
    잘 해놓고 어처구니없는 배열 사이즈 실수를 했다
    * before
    dp = [0] * 100
    * after
    dp = [0] * 101
'''
