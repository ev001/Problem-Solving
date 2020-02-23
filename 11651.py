import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a.sort(key=lambda x: (x[1], x[0]))
    for x in a:
        print(x[0], x[1], end="\n")

'''
    처음에 제출 하였을 때는 for문 아래에 
    print(x) 하여 리스트 형식으로 제출하였다.
    당연히 틀렸다. 왜냐하면 [1,-1]\n[1,2]\n... 
    이런식으로 대괄호 및 콤마가 찍히기 때문!
    
    문장 마지막에 어떻게 처리할지 정해주는 end를
    사용하여 개선하였다. print(x[0], x[1], end="\n") 
'''