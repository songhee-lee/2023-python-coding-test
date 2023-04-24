n = int(input())
array = list(map(int,input().split()))

def binary_search_loop (array,start,end):
    while start <= end:
        mid = (start+end)//2

        ## 현재 중간점 위치가 고정점일 경우
        if array[mid]==mid: 
            print(mid)
            exit(0)
        # 현재 중간점 인덱스가 수열의 값보다 작을 경우, 좌측 리스트 확인
        elif array[mid] > mid : end = mid-1
        # 현재 중간점 인덱스가 수열의 값보다 클 경우, 우측 리스트 확인
        else : start = mid+1
    return -1

print(binary_search_loop(array,0,n-1))

