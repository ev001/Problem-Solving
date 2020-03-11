# 거스름돈 # 그리디

n = int(input())
money = 1000 - n
coin = 0
while money:
    for num in [500, 100, 50, 10, 5, 1]:
        while money >= num:
            money -= num
            coin += 1

print(coin)
