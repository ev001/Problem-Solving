# 점수 계산 # 구현

# 개선코드
score = [[i + 1, int(input())] for i in range(8)]
score.sort(key=lambda x: -x[1])
problem = []
sum_score = 0

for i in range(5):
    sum_score += score[i][1]
    problem.append(str(score[i][0]))

problem.sort()
print(sum_score)
print(" ".join(problem))

# 초기 코드

# a = []
# for i in range(8):
#     inner = []
#     n = int(input())
#     inner.append(i + 1)
#     inner.append(n)
#     a.append(inner)
#
# a.sort(key=lambda x: -x[1])
# b = a[:5]
# b.sort(key=lambda x: x[0])
# sum = 0
# ans = []
# for i in b:
#     sum += i[1]
#     ans.append(str(i[0]))
#
# print(sum)
# print(' '.join(ans))

'''
    join 단점 str 만 사용 가능 int인경우 str 로 변경의 불편함.
    => for문을 통해서 print(i, end =' ') 와 같이 end를 사용할 수도..
    # for i in sorted(problem):
    # print(i, end = ' ')
'''