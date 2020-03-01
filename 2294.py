# 동전2 # DP
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for i in range(k + 1)]
coins = [int(input()) for _ in range(n)]

for idx in range(1, k + 1):
    temp = []
    for coin in coins:
        if idx - coin >= 0 and dp[idx - coin] != -1:
            temp.append((dp[idx - coin] + 1))

    if not temp:
        dp[idx] = -1
    else:
        dp[idx] = min(temp)

print(dp[k])

'''
    교훈 및 배운점
    
    리스트에 요소가 있는지 검사할때에는 
    
    if len(list): 를 지양하고,
   
    if not list:
        ...
    else:
        ...
    를 지향 해야 한다.
    
    파이썬 스타일 가이드 참조
'''
