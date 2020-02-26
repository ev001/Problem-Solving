# 듣보잡 # 구현
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set(input().strip() for _ in range(N))
see = set(input().strip() for _ in range(N))

ans = listen & see
print(len(ans))
print("\n".join(sorted(ans)), flush=True)

'''
    귀찮아서 sys.stdin.readline 안썼는데 
    안쓰니까 계속 런타임 에러 발생 ..
    귀찮더라도 사용하기 
'''