'''
[설명]
- 처음에 트럭이 있는 본부는 1번 마을 왼쪽에 있다.
- 트럭은 본부에서 출발하여 1번 마을부터 마지막 마을까지 오른쪽으로 가면서 물건을 배송한다.
- 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호, 보낼 박스의 개수를 안다.
    - 박스는 크기가 모두 동일하다.
    - 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 존재한다.
- 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.
- 아래의 조건을 모두 만족하면서 '배송할 수 있는 최대 박스 수'를 구하라

[조건]
1. 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
2. 트럭은 지나온 마을로 되돌아가지 않는다.
3. 박스들 중 일부만 배송할 수도 있다.

[아이디어]
- 도착지 기준으로 오름차순 정렬
- 
-> ✅ 다시풀기
'''
import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

dlvy = []
for _ in range(m):
    box_info = list(map(int, sys.stdin.readline().split()))
    dlvy.append(box_info)

dlvy.sort(key=lambda x:(x[1], x[0]))

box = [0] * (n + 1)
ret = 0
for s, d, b in dlvy:
    _max = b
    for i in range(s, d):
        _max = min(_max, c - box[i])
    
    for i in range(s, d):
        box[i] += _max
    
    ret += _max

print(ret)