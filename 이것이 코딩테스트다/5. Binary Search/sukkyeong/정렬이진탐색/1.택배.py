'''
1. 트럭용량만크므 박스개수를 담음
2. 박스를 배송하면서
3. 부족한 만큼 박스를 담음(근데 지나온건 패스)
4. 다시 또 배송
5. 마지막까지 완주 후 박스 개수를 리턴함

1. 출발지, 도착지, 박스개수를 저장하고 도착지 오름차순으로 정렬한다.
2. 각 마을에서의 트럭 용량을 기록할 배열을 만든다.
3. 출발지-도착지 사이 마을의 트럭 용량에서 박스 개수만큼을 뺀다. ( 박스개수가 트럭용량보다 작을경우 트럭용량을 뺀다 )
4. 지금까지 뺐던 박스 총 개수를 반환한다.
'''
import sys

input = sys.stdin.readline
n, space = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
send = []
answer = 0
# [받는 마을, 보내는 마을] 순으로 정렬한다.
for i in range(m):
    a, b, amount = map(int, input().split())
    send.append([a, b, amount])
send.sort(key=lambda x: (x[1], x[0]))

for start, destination, boxes in send:
    maxbox = boxes
    # start부터 dest까지 얼만큼 박스를 보낼 수 있는지 검사
    for i in range(start, destination):
        maxbox = min(maxbox, space - box[i])
    # 박스를 담는 동시에 answer 또한 +, 어차피 담은 박스는 반드시 배달된다.
    for i in range(start, destination):
        box[i] += maxbox
    answer += maxbox
print(answer)
