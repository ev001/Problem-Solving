import sys

input = sys.stdin.readline

plus, minus = [], []
zero, one = 0, 0

N = int(input())
for _ in range(N):
    tmp = int(input())

    if tmp == 1:
        one += 1
    elif tmp == 0:
        zero += 1
    elif tmp > 0:
        plus.append(tmp)
    else:
        minus.append(tmp)

    plus.sort(reverse=True)
    minus.sort()

if len(plus) % 2 == 1:
    plus.append(1)

if len(minus) % 2 == 1:
    minus.append(0 if zero > 0 else 1)

ans = one

for i in range(0, len(plus), 2):
    ans += plus[i] * plus[i + 1]

for i in range(0, len(minus), 2):
    ans += minus[i] * minus[i + 1]

print(ans)
