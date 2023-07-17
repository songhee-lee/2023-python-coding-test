from collections import defaultdict

def solution(tickets):
	# {출발지 : [도착지]} 저장하기
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    
    for k in graph:	# 도착지가 여러개면 알파벳 순으로 정렬
        graph[k].sort(reverse=True)
    
    n = len(tickets)
    now = "ICN"
    stack = ["ICN"] # 현재 경로
    answer = []     # 정답 경로
    while stack :
        now = stack[-1]     # 현재 위치
        # 현재 위치에서 다음에 갈 수 있는 경로가 없을 때, 
        # 즉 마지막 위치를 정답 경로에 추가하기
        if now not in graph or not graph[now]:
            answer.append(stack.pop())
        # 다음에 갈 수 있는 경로가 있으면 알파벳 순서로 추가하기
        else:
            stack.append(graph[now].pop())
    
    return answer[::-1]