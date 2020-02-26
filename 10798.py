import sys

input = sys.stdin.readline

a = [[] for i in range(15)]

for _ in range(5):
    cnt = 0
    for i in (input().strip()):
        a[cnt].append(i)
        cnt += 1

for i in a:
    print("".join(i), end='')

'''
    고민했던것
    1. 어떻게 세로로 뽑을것인가.?
        - row당 최대 길이가 주어져 있어 빈 리스트를 만들어놓는다
    2. 어떻게 채울것인가?
        - 만들어놓은 리스트에 cnt 변수를 두어
        - input을 cnt 인덱스에 차례로 넣어주고 cnt 초기화
    3. 어떻게 print 할것인가?
        - list => str 해주는 join을 이용
        - end 조건으로 '' 를 주어 이어서 출력
         
    고찰
    파이썬으로 언어를 바꾼지 얼마 안됐는데 
    초등부 문제라고 자만해 너무 많은 시간을 썼다.
    
    배열을 가지고 노는 문제를 더 풀어봐야겠다.
    
    * other code *
    
    text = []
    for i in range(5):
        text.append(input())

    for i in range(max([len(e) for e in text])):
        for j in range(5):
            if i < len(text[j]):
                print(text[j][i], end="")
'''