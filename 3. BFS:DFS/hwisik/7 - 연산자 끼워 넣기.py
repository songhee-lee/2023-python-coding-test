'''
1. 사용할 수 있는 연산자와 숫자에 대해서 재귀적으로 탐색한다.
2. 만약, 모든 수를 탐색했다면, 최대값과 최솟값을 갱신한다.
'''

# DFS - Ver.1
def dfs(idx, total):
    global min_ret, max_ret
    
    # 모든 수 탐색했으면, 최소값과 최대값 갱신
    if idx == len(nums):
        min_ret = min(min_ret, total)
        max_ret = max(max_ret, total)
        return
    
    # 사용할 수 있는 연산자에 대해 탐색
    for i in range(4):
        tmp = total
        if op[i] > 0:
            if i == 0: total += nums[idx]
            if i == 1: total -= nums[idx]
            if i == 2: total *= nums[idx]
            if i == 3: total = int(total / nums[idx])
            
            op[i] -= 1 # 연산자 사용했다.
            dfs(idx + 1, total) #
            total = tmp # 다음 계산을 위해 원래 값으로 되돌린다.
            op[i] += 1 # 연산자도 채워넣는다.
   
# DFS - Ver.2   
def dfs2(idx, total, plus, minus, mul, div):
    global min_ret, max_ret
    if idx == len(nums):
        min_ret = min(min_ret, total)
        max_ret = max(max_ret, total)
        return
    if plus: dfs2(idx + 1, total + nums[idx], plus - 1, minus, mul, div)
    if minus: dfs2(idx + 1, total - nums[idx], plus, minus - 1, mul, div)
    if mul: dfs2(idx + 1, total * nums[idx], plus, minus, mul - 1, div)
    if div: dfs2(idx + 1, int(total / nums[idx]), plus, minus, mul, div - 1)
    

n = int(input())
nums = list(map(int, input().split())) # 숫자
op = list(map(int, input().split())) # 연산자 (+, -, *, //)

min_ret = float('inf')
max_ret = float('-inf')

dfs(1, nums[0]) # DFS 

print(max_ret)
print(min_ret)