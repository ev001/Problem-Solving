# 뒤집기 # 그리디

n = list(map(int, input().strip()))
n.append(5)
cnt_0 = 0
cnt_1 = 0
for i in range(len(n)-1):
    if n[i] != n[i + 1]:
        if n[i] == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))
