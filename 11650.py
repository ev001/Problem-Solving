import sys
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a.sort(key=lambda x: (x[0], x[1]))
for i in a:
    print(i[0], i[1])

'''
    sort 인자 설명
    아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
    아이템 두 번째 인자를 기준으로 오름차순으로 정렬을 한다.
    
    만약 첫번째 인자는 오름차순, 두번째 인자는 내림차순으로 하고싶으면
    key = lambda x : (x[0], -x[1]))
    와 같이 한다.
'''
