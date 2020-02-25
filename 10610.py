import sys

input = sys.stdin.readline

N = list(input().strip())

if sum(map(int, N)) % 3 == 0 and "0" in N:
    print("".join(sorted(N, reverse=True)))

else:
    print(-1)

'''


# for i in range(len(N)):
#     value += N[i] * pow(10, (len(N) - (i + 1)))
# if value % 30 == 0:
#     print(value)
# else:
#     print(-1)

    처음에는 위와 같이 숫자를 제곱해서 문제를 해결하고자 하였음.
    그랬더니 시간초과 발생.

    파이썬의 장점인 문자열을 이용해 문제를 풀고자함.

    고려한것 
    1. 3의 배수 판정법 
    2. 각 자리 수는 0~9 범위. 따라서 str 상태로 sort OK!   

    어려웠던 점.
    1. join 함수    
        join은 문자열 관련 함수인데 int 형으로 list를 만들어
        계속 오류를 발생
    2. 그외 파이썬 빌트인 함수들 .. 
'''
