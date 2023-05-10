""" 
결과 최댓값과 최솟값 출력 하기
"""

# 1. 입력 받기
N = int(input())
numbers = list(map(int, input().split()))     # 숫자
plus, minus, mul, div = map(int, input().split())   # 연산자 + - x /

# 최댓값, 최솟값 초기화
res_max, res_min = -1e9, 1e9

def calculate(numbers, now, plus, minus, mul, div):
    global res_max, res_min
    
    if numbers :
        if plus:
            calculate(numbers[1:], now+numbers[0], plus-1, minus, mul, div)
        if minus:
            calculate(numbers[1:], now-numbers[0], plus, minus-1, mul, div)
        if mul:
            calculate(numbers[1:], now*numbers[0], plus, minus, mul-1, div)
        if div:
            if now > 0 :
                calculate(numbers[1:], now//numbers[0], plus, minus, mul, div-1)
            elif now == 0:
                calculate(numbers[1:], 0, plus, minus, mul, div-1)
            else:
                calculate(numbers[1:], -((-now)//numbers[0]), plus, minus, mul, div-1)

    # 모든 숫자 다 사용한 경우 최대/최소 업데이트
    else:
        res_max = now if now > res_max else res_max
        res_min = now if now < res_min else res_min 
        

calculate(numbers[1:], numbers[0], plus, minus, mul, div)

print(res_max)
print(res_min)