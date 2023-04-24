'''
공항에는 g개의 탑승구, 각 1~g번 번호 부여
p개의 비행기를 순서대로 배치하다가 어떠한 탑승구도 불가능하면 운행 중지
최대한 많은 비행기를 배치하는 방법
'''

def find_set(parents, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x:
        parents[x] = find_set(parents, parents[x])
    return parents[x]

def union_set(parents, a, b):
    a = find_set(parents, a)
    b = find_set(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

num_gates = int(input())  # 탑승구의 개수 입력받기
num_planes = int(input())  # 비행기의 개수 입력받기

parents = [0] * (num_gates + 1)  # 부모 테이블 초기화
for i in range(1, num_gates + 1):
    parents[i] = i  # 부모를 자기 자신으로 초기화

result = 0
for _ in range(num_planes):
    current_gate = find_set(parents, int(input()))  # 현재 비행기의 탑승구의 루트 확인
    if current_gate == 0:  # 현재 루트가 0이면 종료
        break
    union_set(parents, current_gate, current_gate - 1)  # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)
