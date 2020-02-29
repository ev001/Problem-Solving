# 기상캐스터 # 구현
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ans = [[-1] * m for _ in range(n)]
a = [list(map(str, input().strip())) for _ in range(n)]

for row in range(n):
    flag, visit = 0, 0
    for col in range(m):
        if flag == 0:
            if a[row][col] != '.':
                ans[row][col] = 0
                flag = 1
        else:
            if a[row][col] == '.':
                ans[row][col] = visit + 1
                visit += 1
            else:
                ans[row][col] = 0
                visit = 0

for row in ans:
    print(" ".join(map(str, row)))

''' 
    생각한 논리        
    flag=0? yes, a값? . 
        -> pass
    flag=0? yes, a 값? c
        -> 해당 좌표 ans값 0 flag=1 
    flag=0? no, a값 .
        //ans의 해당값? -1 
            -> ans(현재좌표) = visit +1     
    flag=0? no, 해당값? c
        -> ans = 0, visit = 0
'''
