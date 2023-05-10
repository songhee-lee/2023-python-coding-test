""" 
- 2초 / 256MB

- D[N] = D[N-1] 각 자리수를 P번 곱한 합
"""

A, P = map(int, input().split())

result = { str(A): 1}   # '숫자' : 수열 번호
prev = A
count = 1
while True:
    numbers = list(map(int, str(prev))) # 숫자를 자릿수별로 분리    

    # 각 자릿수 P 번 곱한 합
    now = 0
    for x in numbers: 
        now += pow(x, P)

    # 해당 숫자가 반복되는지 확인
    if str(now) in result:
        break
    else:
        result[str(now)] = count + 1
        count += 1
        prev = now

print(result[str(now)]-1)