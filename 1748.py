# 수 이어 쓰기 1 # 구현

a = int(input())
nSum = 0
for i in range(len(str(a)) - 1):
    nSum += 9 * (10 ** i) * (i + 1)
nSum += (a - (10 ** (len(str(a)) - 1)) + 1) * len(str(a))
print(nSum)

'''
    # nSum = ""
    # for i in range(1, a + 1, 1):
    #     nSum = nSum + "".join(str(i))
    # print(len(nSum))
    처음에는 위와같이 풀었다.
    당연히 시간초과 발생
    
    1~9         1 * 1 * 9
    10~99       2 * 10 * 9
    100~999     3 * 100* 9
    1000~9999      ...

    이 문제는 위와 같은 자리수의 규칙이 있음.
    만약 3자리라면 2자리까지 위와 같은 방식으로 계산해주고
    
    마지막 3자리수 부분은 input_num - 10^(자리수-1) + 1 로
    구한 값을 3을 곱하여 계산한것에 더해준다.
'''


