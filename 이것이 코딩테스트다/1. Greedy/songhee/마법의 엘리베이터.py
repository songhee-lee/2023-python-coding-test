"""Pseudo Code
1의 자리 수부터 자릿수 맞추기
1. 5보다 작으면 down
2. 5보다 크면 up
3. 5일 때는, 올라가는게 유리한지 내려가는게 유리한지 계산 후 up or down
"""

def solution(storey):
    answer = 0
    
    # 예외. 10보다 작을 때
    if storey < 10 :
        return min(storey, 10 - storey + 1)
    
    # 10의 배수 단위로 버튼 선택
    while storey > 0 :
        x = storey % 10
        
        # 1) 5보다 크면 up
        if x > 5 :
            storey += 10 - x
            answer += 10 - x

        # 2) 5보다 작으면 down
        elif x < 5 :
            storey -= x
            answer += x

        # 3) 5와 같으면 올라갈 때와 내려갈 때 어느게 유리한지 계산
        elif x == 5 :
            
            # 올라가는 경우, 다음 step
            up = ((storey + x) // 10) % 10
            up = min(up, 10 - up)

            # 내려가는 경우, 다음 step
            down = ((storey - x) // 10) % 10
            down = min(down, 10 - down)
            
            if up > down :
                storey -= x
            else :
                storey += 10 - x
                
            answer += 5
            
        storey //= 10
    
    return answer



########
### 재귀 풀이
def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))