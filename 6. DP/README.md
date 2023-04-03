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

<br><br><br>

### 문제

|                    | 송희                                                         | 숙경 | 주현 | 휘식 |
| ------------------ | ------------------------------------------------------------ | ---- | ---- | ---- |
| 1로 만들기         | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/01.%201%EB%A1%9C%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py) |      |      |      |
| 개미 전사          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/02.%20%EA%B0%9C%EB%AF%B8%20%EC%A0%84%EC%82%AC.py) |      |      |      |
| 바닥 공사          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/03.%20%EB%B0%94%EB%8B%A5%20%EA%B3%B5%EC%82%AC.py) |      |      |      |
| 효율적인 화폐 구성 | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/04.%20%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8%20%ED%99%94%ED%8F%90%20%EA%B5%AC%EC%84%B1.py) |      |      |      |
| 금광               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/05.%20%EA%B8%88%EA%B4%91.py) |      |      |      |
| 정수 삼각형        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/06.%20%EC%A0%95%EC%88%98%20%EC%82%BC%EA%B0%81%ED%98%95.py) |      |      |      |
| 퇴사               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/07.%20%ED%87%B4%EC%82%AC.py) |      |      |      |
| 병사 배치하기      | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/08.%20%EB%B3%91%EC%82%AC%20%EB%B0%B0%EC%B9%98%ED%95%98%EA%B8%B0.py) ✅ |      |      |      |
| 못생긴 수          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/09.%20%EB%AA%BB%EC%83%9D%EA%B8%B4%20%EC%88%98.py) ✅ |      |      |      |
| 편집 거리          | [code ](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/10.%20%ED%8E%B8%EC%A7%91%20%EA%B1%B0%EB%A6%AC.py) ✅ |      |      |      |
| 타일 채우기        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/11.%20%ED%83%80%EC%9D%BC%20%EC%B1%84%EC%9A%B0%EA%B8%B0.py) |      |      |      |
| 파도반 수열        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/12.%20%ED%8C%8C%EB%8F%84%EB%B0%98%20%EC%88%98%EC%97%B4.py) |      |      |      |
| 합분해             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/13.%20%ED%95%A9%EB%B6%84%ED%95%B4.py) ✅ |      |      |      |
| 암호코드           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/14.%20%EC%95%94%ED%98%B8%EC%BD%94%EB%93%9C.py) |      |      |      |
| 이동하기           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/15.%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0.py) |      |      |      |
| 점프               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/16.%20%EC%A0%90%ED%94%84.py) |      |      |      |
| 팰린드롬?          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/17.%20%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC.py) |      |      |      |
| 동전1              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/18.%20%EB%8F%99%EC%A0%841.py) ✅ |      |      |      |
| 동전2              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/19.%20%EB%8F%99%EC%A0%842.py) |      |      |      |
| 내리막길           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/20.%20%EB%82%B4%EB%A6%AC%EB%A7%89%20%EA%B8%B8.py) |      |      |      |
| 파일 합치기        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/21.%20%ED%8C%8C%EC%9D%BC%20%ED%95%A9%EC%B9%98%EA%B8%B0.py) |      |      |      |
| 행렬 곱셈 순서     | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/22.%20%ED%96%89%EB%A0%AC%20%EA%B3%B1%EC%85%88%20%EC%88%9C%EC%84%9C.py) |      |      |      |
| 구간 나누기        | [code ](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/23.%20%EA%B5%AC%EA%B0%84%20%EB%82%98%EB%88%84%EA%B8%B0.py)✅ |      |      |      |
| 자두나무           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/24.%20%EC%9E%90%EB%91%90%EB%82%98%EB%AC%B4.py) ✅ |      |      |      |
| 타일 코드          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/25.%20%ED%83%80%EC%9D%BC%20%EC%BD%94%EB%93%9C.py) |      |      |      |
| 기타리스트         | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/26.%20%EA%B8%B0%ED%83%80%EB%A6%AC%EC%8A%A4%ED%8A%B8.py) |      |      |      |
| 1학년              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/27.%201%ED%95%99%EB%85%84.py) |      |      |      |
| 크리보드           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/28.%20%ED%81%AC%EB%A6%AC%EB%B3%B4%EB%93%9C.py) |      |      |      |
| 출근 기록          | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/29.%20%EC%B6%9C%EA%B7%BC%20%EA%B8%B0%EB%A1%9D.py) ✅ |      |      |      |
| BOJ 거리           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/6.%20DP/songhee/30.%20BOJ%20%EA%B1%B0%EB%A6%AC.py) |      |      |      |
|                    |                                                              |      |      |      |
|                    |                                                              |      |      |      |
|                    |                                                              |      |      |      |
|                    |                                                              |      |      |      |

