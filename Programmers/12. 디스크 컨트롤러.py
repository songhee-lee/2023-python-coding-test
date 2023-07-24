"""
작업의 요청부터 종료까지 걸린 시간의 평균의 최솟값 리턴하기 (소수점 이하 버림)
각 작업에 대해 [요청되는 시점, 작업 소요시간]이 주어진다. 
1 <= 작업 개수 <= 500

(기다린 시간 + 처리 시간)을 최소로 해야되므로 일찍 끝나는 작업부터 해야 된다.
"""
import heapq

# 다음에 올 작업 추가하기
def add_jobs(now, jobs, heap) :
    # 작업이 남았는데 heap이 비어있는 경우, 1개 무조건 추가하기
    if not heap and jobs :      
        st, time = jobs.pop()
        heapq.heappush(heap, (time, st))
    
    # 남은 작업들 중 "기다리고 있는" 작업 추가
    while jobs :
        st, time = jobs.pop()
        if st <= now :
            heapq.heappush(heap, (time, st))
        else :
            jobs.append((st, time))
            return heap
    return heap
        
def solution(jobs) :
    jobs.sort(reverse=True)         # 시작시점 기준으로 정렬
    now = jobs[-1][0]               # 가장 빠른 시작 시점
    heap = add_jobs(now, jobs, [])  # 수행할 작업 리스트
    answer = []
    
    while heap :
        time, st = heapq.heappop(heap)      # 처리 시간, 시작 시간
        answer.append(max(now-st, 0)+time)  # 기다린 시간 + 처리 시간 추가
        now = now + time                    # 현재 시각 변경
        heap = add_jobs(now, jobs, heap)    # 수행할 작업 리스트 업데이트
    
    return sum(answer) // max(len(answer), 1)