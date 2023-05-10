
n,m,l = map(int,input().split())
arr = [0]+sorted(list(map(int,input().split())))+[l]
print(f'arr = {arr}')

start,end = 1,l-1
result = 0

while start <= end:
    mid = (start+end)//2
    print(f'현재 mid = {mid}')
    count = 0
    for i in range(1,len(arr)):
        interval = arr[i]-arr[i-1]
        print(f'interval = arr[i]-arr[i-1] = arr[{i}]-arr[{i-1}] = {arr[i]}-{arr[i-1]} = {arr[i]-arr[i-1]} = {interval}')
        if interval > mid :
            print(f'interval > mid : {interval} > {mid}')
            #print(f'interval-1//mid = {interval}-1//{mid}')
            count = count + ((interval-1)//mid)
            print(f'count 업데이트 : count = {count}')
        elif interval < mid :
            print(f'interval < mid : {interval} < {mid}')
        else : print(f'interval == mid : {interval} == {mid}')
    print(f'count = {count}, mid = {mid}')
    if count > m :
        start = mid+1
    else : 
        end = mid-1
        result = mid
    print(f'start, end 업데이트 : start = {start}, end = {end}, result = {result}')
print(result)


# 휴게소 세우기
# N, M, L = map(int, input().split())
# arr = [0]+list(map(int, input().split()))+[L]
# arr.sort()
# print(f'현재 휴게소 위치 : {arr}')

# start, end = 1, L-1
# result = 0
# while start <= end:
#     print(f'start = {start}, end = {end}')
#     count = 0
#     mid = (start+end) // 2
#     print(f'가장 멀리 떨어져 있는 휴게소 사이의 거리 mid = {mid}')
#     for i in range(1, len(arr)):
#         # 현재 거리 중 mid보다 큰 거리를 찾아서
#         print(f'{i-1}번째 휴게소 위치 : {arr[i-1]}, {i}번쨰 휴게소 위치 : {arr[i]}, 두 휴게소 간 거리 : {arr[i]-arr[i-1]} , mid = {mid} ')
#         if arr[i]-arr[i-1] > mid:
#             # 나눈 만큼 휴게소를 설치 (현재 설치 돼있는 구역은 제외해야해서 -1)
#             print(f'(arr[i]-arr[i-1]-1)//mid = (arr[{i}]-arr[{i-1}]-1)//mid = ({arr[i]}-{arr[i-1]}-1)//{mid}={(arr[i]-arr[i-1]-1)//mid}')
#             count += (arr[i]-arr[i-1]-1)//mid
#             print(f'count = {count}')
#     print(f'count = {count} , M = {M}')
#     if count > M:       # 설치해야 할 개수가 M보다 크면 mid는 더 길어야한다
#         print(f'설치해야 할 개수={count}가 M={M}보다 크면 mid={mid}는 더 길어야한다')
#         print(f'기존 start = {start}')
#         start = mid+1
#         print(f'start 업데이트 : {start}')
#     else:               # 설치해야 할 개수가 M보다 작으면 mid는 더 짧아야한다
#         print(f'설치해야 할 개수={count}가 M={M}보다 작으면 mid={mid}는 더 짧아야한다')
#         print(f'기존 end = {end}')
#         end = mid-1
#         result = mid
#         print(f'end 업데이트 : {end}')
#         print(f'조건은 만족했으므로 result = mid = {mid}')
# print(result)

"""
# 최대힙을 이용하여 구현 : 실패

from heapq import heappush,heappop
from math import ceil,floor

n,m,l = map(int,input().split())    # n:휴게소 위치, m:설치할 개수, l:고속도로 길이
rests = sorted(list(map(int,input().split())))
print(f'설치된 휴게소의 위치 : {rests}')

# 간격 구하기 : 최대힙
intervals = []
for i in range(n-1):
    heappush(intervals,(rests[i]-rests[i+1],rests[i]))
    print(f'앞 휴게소 위치 : {rests[i]}, 뒤 휴게소 위치 : {rests[i+1]}, 두 휴게소 간 간격 : {rests[i]-rests[i+1]}')
    print(f'지금까지의 invervals = {intervals}')
heappush(intervals,(-rests[0],0))          # 시작-첫번째 휴게소 간격
heappush(intervals,(rests[-1]-l,rests[-1])) # 마지막 휴게소-끝 간격
print(f'최종 invervals = {intervals}')

# 휴게소 m개 설치
while m and intervals :
    print(f'지어야 하는 휴게소 개수 : {m}')
    interval,rest = heappop(intervals)
    print(f'앞 휴게소 위치 : {rest} 일 때 간격이 최대 : {interval}')
    if rest == l-1 : 
        print('휴게소 끝에 세울 수 없음')
        continue           # 휴게소 위치가 고속도로 끝보다 1 앞에 위치할 경우 PASS (고속도로 끝에는 휴게소를 세울 수 없기 떄문)
    heappush(intervals,(-ceil((-interval)/2),rest+floor((-interval)/2)))
    heappush(intervals,(-floor((-interval)/2),rest))
    print(f'기존 정보 업데이트 >> 앞 휴게소 위치 : {rest}, -간격 : {-floor((-interval)/2)}')
    print(f'새로운 휴게소 정보 업데이트 >> 앞 휴게소 위치 : {rest+(-interval)//2}, -간격 : {-ceil((-interval)/2)}')
    print(f'invervals 업데이트 >> {intervals}')
    m-=1

print(-intervals[0][0])
"""