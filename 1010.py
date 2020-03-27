# 다리놓기 # dp

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())

    k = m - n
    answer = 1

    while m > k:
        answer *= m
        m -= 1

    while n:
        answer = answer // n
        n -= 1

    print(answer)

'''
    dp인데 그냥 수학으로 풀어버렸다.
'''
