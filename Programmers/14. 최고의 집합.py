def solution(n, s):    
    if n > s: return [-1]
    
    q, r = s // n, s % n
    answer = [q] * n
    
    idx = 0
    while r > 0:
        answer[idx] += 1
        idx += 1
        r -= 1
    
    return answer[::-1]