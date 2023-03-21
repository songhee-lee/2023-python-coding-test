""" 
- A에서 가장 긴 증가하는 부분 수열의 길이 구하기
"""

N = int(input())
numbers = list(map(int, input().split()))

array = [0]
for num in numbers: 
    if array[-1] < num :        # 마지막 숫자보다 큰 경우 수열에 추가
        array.append(num)
    else:                       # 작은 경우
        s, e = 0, len(array)    # 수열 내에서 해당 숫자가 들어갈 곳 확인
    
        while s < e:
            m = (s+e) // 2
            if array[m] < num:
                s = m+1
            else:
                e = m
        array[e] = num

print(len(array)-1)
