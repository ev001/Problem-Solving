import sys
input = sys.stdin.readline

dic = {}
ans = []
N = int(input())

for _ in range(N):
    a = int(input().strip())
    if a in dic:
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1

max_num = max((dic.values()))
for key, value in dic.items():
    if value == max_num:
        ans.append(key)

print(min(ans))