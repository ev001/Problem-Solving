import sys
input = sys.stdin.readline
N = int(input())
maximum = 10001

arr = [0] * maximum

for _ in range(N):
    a = int(input().strip())
    arr[a] += 1
    
for i in range(maximum):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
            
'''
다른사람 코드 (딕셔너리 사용)
    import sys
    N = int(input())

    dic = {}

    for i in range(N):
        a = int(sys.stdin.readline())

        if a in dic:
            dic[a] =  dic[a] +1

        else:
            dic[a] = 1

    for sorted in sorted(dic.items()):
        for i in range(sorted[1]):
            print(sorted[0])

'''