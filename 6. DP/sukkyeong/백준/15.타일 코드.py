import sys  # sys 모듈을 import 합니다.
# 입력 속도를 높이기 위해 input() 함수 대신 sys.stdin.readline() 함수를 사용합니다.
input = sys.stdin.readline

n = int(input())  # 정수 n을 입력 받습니다.

arr = [0 for _ in range(n+1)]  # 길이가 n+1이고 모든 값이 0인 리스트 arr을 생성합니다.
arr[0] = 1  # arr[0]에 1을 할당합니다.
arr[1] = 1  # arr[1]에 1을 할당합니다.

for i in range(2, n+1):
    arr[i] = arr[i-1]+arr[i-2]*2

# n이 홀수인 경우와 짝수인 경우에 대해 결과를 계산하여 출력합니다.
if n % 2 == 1:  # n이 홀수인 경우
    print((arr[n]+arr[n//2])//2)
else:  # n이 짝수인 경우
    print((arr[n]+arr[n//2]+arr[n//2-1]*2)//2)
