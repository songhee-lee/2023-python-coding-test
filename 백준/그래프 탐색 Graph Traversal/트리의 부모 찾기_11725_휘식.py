# 트리의 루트를 1로 가정, 각 노드의 부모 노드를 출력
import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

# 부모 노드를 저장할 리스트
# e.g. parent[1] = 3 -> 노드 1의 부모 노드는 3번 노드
parent = [0] * (n + 1) 
parent[1] = 1 # 루트 노드는 자기 자신이 부모 노드

for _ in range(n - 1):
  a, b = map(int, sys.stdin.readline().split())
  # 양방향 그래프
  tree[a].append(b)
  tree[b].append(a)

# DFS
def dfs(start):
  for nxt in tree[start]:
    if parent[nxt] == 0: # 양방향이기 때문에, 부모를 이미 찾은 노드일 경우 예외 처리 
      parent[nxt] = start # 부모 설정
      dfs(nxt)

dfs(1)

for _ in range(2, n + 1):
  print(parent[_])