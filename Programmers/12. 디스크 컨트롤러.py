import heapq

def solution(jobs):
    answer = 0
    # 처리한 작업 개수, 이전 작업의 요청 시간, 이전 작업의 소요(종료) 시간
    processed_count, prev_start, prev_end = 0, -1, 0
    q = [] 
    
    # 주어진 작업을 모두 처리하기 전 까지
    while processed_count < len(jobs):
        for job in jobs:
            # 현재 작업의 요청 시간이 이전 작업의 요청 시간과 소요(종료) 시간 사이에 존재한다면,
            if prev_start < job[0] <= prev_end:
                heapq.heappush(q, (job[1], job[0])) # 소요시간을 기준으로 넣어준다.
        
        # 처리해야 할 작업이 있다면
        if q:
            need_time, start_time = heapq.heappop(q) # 현재 작업의 소요 시간, 요청 시간
            prev_start = prev_end # 이전 요청 시간은 이전 작업의 소요(종료) 시간으로 갱신
            prev_end += need_time # 이전 소요(종료)시간은 현재 작업의 소요시간을 더해서 갱신 -> 즉, 현재 작업의 종료 시간
            answer += (prev_end - start_time) # 총 소요된 시간을 더해준다.
            processed_count += 1 # 처리한 작업의 개수 + 1
        else:
            # 먼저 요청이 들어온 작업부터 heap에 넣기 위해서
            # 하드디스크가 작업을 수행하고 있지 않을 때, 이전 종료 시간을 늘려준다.
            prev_end += 1
            
    return answer // len(jobs) # 평균