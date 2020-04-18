import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = deque(deque(map(int, input().split())) for _ in range(n))
test = [list(map(int, input().split())) for _ in range(t)]

# 0으로 회전 : 시계방향. 1이면 반시계방향
# 원판에 적힌 수를 더할 변수 하나

for tt in test:
    circles = list()
    x, d, k = tt[0], tt[1], tt[2]
    cnt = 1
    # 배수 찾기
    while True:
        temp = cnt * x
        if temp <= n:
            circles.append(temp)
            cnt += 1
        else:
            break
    # 회전 부분
    for c in circles:
        if d == 0:
            arr[c - 1].rotate(1 * k)
        else:
            arr[c - 1].rotate(-1 * k)
    # print(arr)
    delete_list = list()
    for idx in range(n):
        for i in range(m):
            if arr[idx][i]:
                if i + 1 < m and (arr[idx][i] == arr[idx][i + 1]):
                    delete_list.append([idx, i + 1])
                if 0 <= i - 1 and (arr[idx][i] == arr[idx][i - 1]):
                    delete_list.append([idx, i - 1])
                if idx + 1 < n and (arr[idx][i] == arr[idx + 1][i]):
                    delete_list.append([idx + 1, i])
                if 0 <= idx - 1 and (arr[idx][i] == arr[idx - 1][i]):
                    delete_list.append([idx - 1, i])
                if i == m - 1 and arr[idx][i] == arr[idx][0]:
                    delete_list.append([idx, 0])
                if i == 0 and arr[idx][i] == arr[idx][m - 1]:
                    delete_list.append([idx, m - 1])

    if delete_list:
        for r, c in delete_list:
            arr[r][c] = 0
    else:
        cnt, sum_ = 0, 0
        for a in arr:
            for e in a:
                if e:
                    sum_ += e
                    cnt += 1
        if cnt == 0:
            break
        mid = float(sum_) / cnt
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    if arr[i][j] > mid:
                        arr[i][j] -= 1
                    elif arr[i][j] < mid:
                        arr[i][j] += 1

sum_ = (map(sum, arr))
print(sum(sum_))
