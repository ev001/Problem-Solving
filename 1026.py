# 보물 # 정렬

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * b[i]

print(ans)

'''
시간복잡도: 1초 1억
ex. for문 O(N), 이중 for문인 경우 O(N^2)
* 1초가 걸리는 입력의 크기
- O(1)
- O(logN)- O(N) : 1억
- O(nLogN): 5백만
- O(N^2) : 1만
- O(N^3) : 500
- O(2^N) : 20
- O(N!): 10

출처: https://dev-ahn.tistory.com/10 [Developer Ahn]
'''
