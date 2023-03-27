## DP

### DP 의 조건

1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

<br>

#### 분할 정복 Divide and Conquer 과 DP

- 공통점 : 문제를 작은 단위로 분할한다.
- 차이점 : DP는 부분 문제가 중복되어 상위 문제를 해결할 때 재활용 되지만, 분할 정복은 분할 문제들이 서로 중복되지 않는다.

<br>

### DP 구현 1) Top-Down

- 큰 문제를 해결하기 위해 작은 문제를 호출 

- Memoization 기법으로, DP table 활용

- 재귀를 활용하기 때문에 recursion depth 관련 오류가 생기지 않도록 주의해야 한다.<br>

  -> `recursionsetrecursionlimit()  `  호출해 재귀 완화

```python
# 한 번 계산된 결과를 기록하기 위한 DP 테이블
dp = [0] * 100

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
	# 종료 조건
	if x == 1 or x == 2:
		return 1
	# 계산한 적 있는 문제라면 그대로 반환
	if dp[x] != 0:
		return dp[x]
	# 아직 계산하지 않은 문제는 점화식 따라 계산
	dp[x] = fibo(x-1) + fibo(x-2)
	return dp[x]
```

<br><br>

### DP 구현 2) Bottom-Up

- 작은 문제부터 답을 도출해 큰 문제를 해결

```python
# 한 번 계산된 결과를 기록하기 위한 DP 테이블
dp = [0] * 100

# 계산이 필요없는 피보나치 수 기록
dp[1] = 1
dp[2] = 1

# 피보나치 함수를 반복문으로 구현
for i in range(3, 100):
  dp[i] = dp[i-1] + dp[i-2]
```



