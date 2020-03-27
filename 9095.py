# 1,2,3 더하기 # dp

# 가지수 찾기. 1,2,3 만 사용 n범위는 11, 중복 o

tc = int(input())
for _ in range(tc):
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    print(dp[n])

'''
1: 1
2: 11 , 2
3: 111 12 21 3 
4: 
가장 끝에올수있는 수는 1,2,3이 될것이다.
'''