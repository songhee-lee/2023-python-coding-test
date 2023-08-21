#풀기
'''
동일한 작업 n개
코어 수 2이상 10,000 이하
한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업 실행
2개 이상의 코어가 남을 경우 앞의 코어부터 작업을 처리

cores : 각 코어의 처리시간이 담긴 배열
return 마지막 작업을 처리하는 코어의 번호를 return
'''

#작업 하나씩 for문 - O(n) 효율성 에러
#우선순위 큐 - 불가능
#이분탐색
#time까지 처리한 작업량
def cntWork(t, c, cl):
    #시간이 0일때 처리할 수 있는 작업량은 코어 개수
    if t == 0:
        return cl
    
    #시간이 0일때 처리한 작업량
    count = cl
    
    #time까지 코어가 처리할 수 있는 작업량 합산
    for i in c:
        count += t//i
    
    return count
    
    
    
    
def solution(n, cores):
    corlen = len(cores)

    #코어 수 보다 처리량이 작으면 종료
    if n < corlen:
        return n
    
    
    low, high= 1, max(cores)*n
    time, work = 0, 0
    
    while (low <= high):
        mid = (low + high)//2
        
        cnt = cntWork(mid, cores, corlen)

        #처리한 작업량보다 n이 크면
        if cnt >= n: 
            high = mid - 1
            time = mid
            work = cnt
        else:
            low = mid + 1
    
    #처리한 작업량과 n의 차이 갱신
    work -= n
    for i in reversed(range(corlen)):
        #time에 작업을 처리하는 core
        if time % cores[i] == 0:
            if work == 0:
                answer = i + 1
                break
            work -= 1

    return answer
