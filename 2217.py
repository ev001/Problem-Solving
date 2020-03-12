# 로프 # 그리디
import sys

input = sys.stdin.readline

n = int(input())
a = [int(input().strip()) for _ in range(n)]
a.sort(reverse=True)

max, cnt = 0, 1
for i in range(n):
    check_max = a[i] * cnt
    if check_max > max:
        max = check_max
    cnt += 1

print(max)

'''
무게 1 부터 점점 증가시키면서 
로프최대중량/ 개수 해서 버틸수 있나 보는식으로 ?

단, 모든로프 사용할 필요 x
 
    3 
 15 20 30 모두 사용 -> 45 
 20 30 사용 -> 40
 15 30 사용 -> 30
 15 20 사용 -> 30
 =? 
 
 5
 1 2 3 4 5 모두사용 -> 5
 2 3 4 5 -> 8
 3 4 5 -> 9
 4 5 -> 8
 5-> 5
 
 잴큰수(정렬) 부터해서 부터 하나씩 하면서 
 최대 max 를 계속 리턴 해주는식으로 모두 해보는걸로
 

'''
