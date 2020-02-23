import sys

input = sys.stdin.readline

def greedy(meeting):
    meeting_count = 0
    start_time = 0

    for meet in meeting:
        if meet[0] >= start_time:
            meeting_count += 1
            start_time = meet[1]
    return meeting_count

if __name__ == "__main__":
    N = int(input())
    meeting = [list(map(int, input().split())) for _ in range(N)]
    meeting.sort(key=lambda x: x[0])
    meeting.sort(key=lambda x: x[1])

    print(greedy(meeting))

'''
    실수한것
    meeting.sort(key=lambda x: (x[0],x[1])) 
    로 정렬을 한번에 해버려서 에러를 발생시킴    
'''