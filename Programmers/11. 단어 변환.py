from collections import deque

INF = int(1e9)
answer = INF

def solution(begin, target, words):
    def diff_only_one(begin, _next):
        diff_count = 0
        for x, y in zip(begin, _next):
            if x != y:
                diff_count += 1
        
        return True if diff_count == 1 else False
    
    def bfs(begin):
        global answer
        q = deque([(begin, 0)])
        while q:
            begin, count = q.popleft()
            
            if begin == target:
                answer = min(answer, count)
                continue
            
            for i, word in enumerate(words):
                if diff_only_one(begin, word) == 1 and count + 1 < change_count[i]:
                    change_count[i] = count + 1
                    q.append((word, change_count[i]))
                
    n = len(words)
    change_count = [INF] * n
    
    if target not in words:
        return 0
    
    bfs(begin)
    
    return answer