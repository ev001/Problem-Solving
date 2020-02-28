_sum = 0
for i in range(10):
    score = int(input().strip())
    _sum += score
    if _sum >= 100:
        if _sum - 100 > 100 - (_sum - score):
            _sum -= score
            break
print(_sum)

