# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

# 입력 받기
G = int(input())    # 탑승구 수
P = int(input())    # 비행기 수
parent = [i for i in range(G+1)]    # 부모 테이블
answer = 0
for _ in range(P):
    # 도킹 가능한 탑숭구 번호 찾기
    x = find_parent(parent, int(input()))
    
    if  x == 0 :    # 도킹 불가능하면 끝!
        break
    union_parent(parent, x, x-1)    # 도킹 가능하면 앞 번호랑 합치기
    answer += 1

print(answer)


"""
q = []
for _ in range(P):
    q.append(int(input()))   # 도킹 가능한 최대 탑승구 번호

docking = set()     # 현재 도킹된 탑승구 번호
for x in q:
    
    finish = True   # 종료 조건 flag
    # 최대 탑승구 ~ 1번까지 차례로 도킹 가능한지 확인하기
    for i in reversed(range(1, x+1)):
        if i not in docking:
            docking.add(i)
            add = False
            break
    
    # 도킹 불가능하면 끝!
    if finish :
        break

print(len(docking))
"""