import sys
from collections import deque
import time

sys.setrecursionlimit(10000)

start_time = time.time() # 측정 시작
# 프로그램 소스코드

n, m = map(int, sys.stdin.readline().split()) # n, m을 공백으로 구분하여 입력받기
min_num = 10001 # 현재 행에서 가장 작은 수 
max_num = 0 # 모든 행에서 가장 큰 수

for _ in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split())) # m개의 수를 공백으로 구분하여 입력받기
    min_num = min(tmp_list) # 현재 줄에서 '가장 작은 수' 찾기
    max_num = max(max_num, min_num) # '가장 작은 수' 중에서 '가장 큰 수' 찾기
    
print(max_num)
    

end_time = time.time() # 측정 종료
print("Time: ", end_time - start_time) # 수행 시간 출력