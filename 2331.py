def next(a, p):
    x = str(a)
    ans = 0
    for i in x:
        ans += (pow(int(i), p))
    return ans


def dfs(a, p, cnt, visited):
    if visited[a] != 0:
        return visited[a] - 1
    visited[a] = cnt
    nxt = next(a, p)
    cnt += 1
    return dfs(nxt, p, cnt, visited)


a, p = map(int, input().split())
visited = [0] * 60000
cnt = 1
print(dfs(a, p, 1, visited))

'''
비재귀를 이용한 다른사람 코드
A, P = input().split()
A = int(A)
P = int(P)


powers = list()

for i in range(0, 10):
    powers.append(i ** P)
# print(powers)

D = list()

D.append(A)
temp = D[0]

while True:
    total = 0
    while temp > 0:
        index = temp % 10
        temp //= 10
        # print(index)
        total += powers[index]
    # print(total)
    if total in D:
        # print("total은 ", total, "입니다")
        temp = total
        break
    else:
        D.append(total)
        temp = D[len(D) - 1]

count = 0

for i in D:
    if temp != i:
        count += 1
    else:
        break
print(count)
'''
