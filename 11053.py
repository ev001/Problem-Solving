# 가장 긴 증가하는 부분 수열 # dp

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

'''
6
10 20 10 30 20 50

10 20 10 30 20 50
01 02 01 03 02 04

arr 리스트를 차례로 돌면서
첫번째부터 자기 자신(1) + 자신보다 작은 수의 개수 ( 첫번째는 없으니까 0)

두번째 = arr 리스트에서 첫번째부터 두번째 인덱스까지 loop 해서 max 값 찾아서
거기다 + 1 
'''
