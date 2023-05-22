# cost[i][j] : i번째 숫자에서 j번째 숫자 누를 때 비용
cost = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3], # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], # 9
]

def solution(numbers):
    numbers = list(map(int, numbers))
    q = {(4, 6): 0}     # 확인해야 할 리스트

    for num in numbers: 
        now_q = {}      # 다음에 확인 할 리스트
        for finger, w in q.items():
            left, right = finger
            
            # 왼쪽 위치와 동일한 경우
            if left == num :
                # 리스트에 추가되지 않았거나 최소 비용이 아닌 경우
                if not (num, right) in now_q or now_q[(num, right)] > w + 1:
                    now_q[(num, right)] = w + 1
            # 오른쪽 위치와 동일한 경우
            elif right == num : 
                # 리스트에 추가되지 않았거나 최소 비용이 아닌 경우
                if not (left, num) in now_q or now_q[(left, num)] > w + 1:
                    now_q[(left, num)] = w + 1
            else:
                if not (num, right) in now_q or now_q[(num, right)] > w + cost[left][num] :
                    now_q[(num, right)] = w + cost[left][num]
                if not (left, num) in now_q or now_q[(left, num)] > w + cost[right][num] :
                    now_q[(left, num)] = w + cost[right][num]
    
        q = now_q
    
    return min(list(q.values()))
