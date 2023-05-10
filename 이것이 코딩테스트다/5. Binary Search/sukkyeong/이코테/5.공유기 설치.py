'''
c개의 공유기를 n개의 집에 적당히 설치
가장 인접한 두 공유기 사이의 거리를 최대
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬
2. start = 1, end = array[-1] - array[0] 으로 설정( 시작값은 최소 거리, 끝 값은 최대 거리 )
3. 앞 집부터 공유기 설치
4. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치
5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정
'''

n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def solution(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]
        # 간격 줄여야 함
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        # 간격 늘려야함
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0
solution(array, start, end)
print(answer)
