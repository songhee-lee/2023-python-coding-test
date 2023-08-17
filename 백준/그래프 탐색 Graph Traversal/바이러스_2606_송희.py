from collections import deque

# 입력 받기
N = int(input())
M = int(input())
networks = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

virus = [0] * (N+1)		# 바이러스에 전염되면 1 아니면 0
# 바이러스 전파하기
q = deque([1])
virus[1] = 1
while q :
    now = q.popleft()

    for nxt in networks[now] :
        if virus[nxt] == 0 :
            q.append(nxt)
            virus[nxt] = 1

print(sum(virus)-1)