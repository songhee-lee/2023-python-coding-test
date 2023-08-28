# 들어올릴 수 있는 물체의 최대 중량 구하기
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
# e.g. 5, 10, 15일 때 모든 로프를 사용하면 최대 15kg까지 들 수 있음
# -> 10, 15만 사용하면 최대 20kg까지 들 수 있음
# -> (증명) 일부의 로프만 사용해도 된다 
n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True) # 내림차순 정렬
max_weight = ropes[0] * 1 # 최대 무게를 버티는 로프 1개만 사용하기

# 최대 무게 찾기
for i in range(1, n):
  # ropes[i]: 현재시점에서 최소 무게를 드는 로프, (i + 1): 사용할 로프 개수
  max_weight = max(max_weight, ropes[i] * (i + 1)) 
  
print(max_weight)