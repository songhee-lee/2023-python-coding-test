import heapq
def solution(n, works):
    answer = 0
    if n >= sum(works):
        return 0
    #모든 원소의 부호를 반대로 하면 max heap 처럼 사용 가능
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    for w in works:
        answer += w ** 2
    return answer

'''
import numpy as np

def solution(n, works):
    answer = 0
    w_len = len(works)
    works.sort()
    while(n):
        #현재 최대값 지정
        #재정렬 없이 현재 최대값은 항상 마지막 인덱스에 위치하도록
        cur_max = works[w_len-1]
        if (np.any(works) == False) : break
        #현재 최대값 이상인 값이 있다면 제거
        for i in range(w_len-1, 0):
            if (np.any(works) == False) : break
            if works[i] >= cur_max:
                works[i] -= 1
                n -= 1
            
            #야근시간 끝
            if (n <= 0) : break
    
    if (np.any(works) == False) : return 0
    for w in works:
        answer += w ** 2
    
    return answer
'''

'''
시간초과
import numpy as np
#works 에서 n 만큼 숫자를 뺄 수 있다.
def solution(n, works):
    answer = 0
    w_len = len(works)
    works.sort(reverse=True)
    i=0
    while (n > 0):
        if (np.any(works) == False) : break
        if i == w_len-1:
            work = works[i] - works[i%(w_len-1)]
        else:
            work = works[i] - works[i+1]
        if work == 0:
            work =1
        
        works[i] -= work
        n -= work
        i += 1
        if (i > w_len-2):
            i = i % w_len
    for w in works:
        answer += w ** 2
        
    return answer
'''
