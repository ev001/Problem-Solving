# 올림픽 # 구현
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank_list = [1] * n
rank, cnt = 1, 1

for now in range(1, len(a)):
    before = now - 1
    if a[now][1] == a[before][1] and a[now][2] == a[before][2] and a[now][3] == a[before][3]:
        rank_list[a[now][0]-1] = rank
        cnt += 1
    else:
        rank_list[a[now][0]-1] = rank + cnt
        rank += cnt
        cnt = 1

print(rank_list[k-1])

''''
    내가 푼것 처럼 변수 많이 안쓰고 if else 안쓰고 
    깔끔하게 풀 수 있을거같은데 다른코드를 고민해봐도
    답이 안나오다가 아래에 첨부한 코드를 보았다.

    * 다른사람 코드 *
    # import sys
    # sys.stdin = open("input.txt", 'r')
    # 
    # N, K = map(int, input().split())
    # country = [0]*N
    # 
    # for i in range(N):
    #     country[i] = list(map(int, input().split()))
    # country.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    # idx = [country[i][0] for i in range(N)].index(K)
    # while country[idx-1][1:] == country[idx][1:]:
    #     idx -= 1
    # print(idx+1)

    이렇게도 생각할 수 있구나 하고 감탄했다 .. 
'''