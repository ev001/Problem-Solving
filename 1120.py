# 문자열 # 그리디

import sys
from collections import deque

input = sys.stdin.readline

a, b = map(str, input().split())
dif = len(b) - len(a)
a, b = deque(a), deque(b)
check = []
b_len = len(b)

for i in range(dif + 1):
    # 케이스 선택 먼저
    front = i  # 0 1 2 ...
    end = dif - i
    for j in range(front, 0, -1):
        a.appendleft(b[j-1])
        print("front",j) # i 는  0부터
    # b[6], b[5] ...
    for k in range(end, 0, -1):
        a.append(b[b_len - k])
        print(k, b_len - k)

    # check 값 구하기.
    cnt = 0
    for i, x in enumerate(b):
        if a[i] != x:
            cnt += 1
    print("a", a)
    print("b", b)
    for j in range(front, 0, -1):
        a.popleft()
    for k in range(end, 0, -1):
        a.pop()


    check.append(cnt)

print(min(check))
''' 
2 03 택배가지러감 
2 52 왔댜. 덩도싸고 중고나라에 당근마켓에도 올리고 ...
3:40 다시시작
a length <= b length
a 앞 or 뒤 알파벳 추가

case 길이차이 + 1 만큼.

     
길이 차이가 2이면? dif 
앞 0 뒤 2에 맞추고 비교. 0, 1 2 
앞 1 뒤 1에 맞춰주고 비교.  
앞 2 에 맞춰주고 비교 인덱스로는 1 먼저 들어가고 0 그다음 들어가고.

    
길이 차이가 3이면?
    앞 셋, 뒤 0
    앞 둘 , 뒤 하나
    앞 하나, 뒤 둘
    앞 0, 뒤 셋

길이차이가 1이면?
     1. 앞 1 뒤 0
     2. 뒤 0 앞 1
'''
