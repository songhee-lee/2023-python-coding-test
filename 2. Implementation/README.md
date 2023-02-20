## 구현 Implementation

- 풀이를 떠올리기는 쉽지만 소스코드로 옮기기 어려운 문제
- **완전 탐색** : 모든 경우의 수를 다 계산하는 해결 방법
- **시뮬레이션** : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 문제 유형
<br><br>

### 제약 사항
1. 파이썬 리스트 크기
    
    ```python
    a[1000] # 4KB
    a[백만]  # 4MB
    a[천만]  # 40MB
    ```
    
    데이터 크기가 **1000만 이상인 리스트가 있다면** 메모리 용량 제한에 걸릴 수 있음!
    <br><br>
    
2. 시간 제한 1초
    - **2천만 번 연산**을 수행하면 무리가 없음
    - 데이터 개수가 100만개이고, 시간복잡도가 O(NlogN) 일 때, 약 2천만이 됨
    - 만약 pypy를 지원하면 이걸 선택하자!
      <br> python3 문법 그대로 따르는데 훨씬 빠르다.


### 문제

| Name           |    송희    |     숙경    |    주현     |     휘식      |
| -------------- | --------- | --------- |--------- |--------- |
| 상하좌우          |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/1%20-%20%EC%83%81%ED%95%98%EC%A2%8C%EC%9A%B0.py)  |  [code] | [code]  | [code]  |
| 시각             |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/2%20-%20%EC%8B%9C%EA%B0%81.py)  |  [code] | [code]  | [code]  |
| 왕실의 나이트      |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/3%20-%20%EC%99%95%EC%8B%A4%EC%9D%98%20%EB%82%98%EC%9D%B4%ED%8A%B8.py)  |  [code] | [code]  | [code]  |
| 게임 개발         |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/4%20-%20%EA%B2%8C%EC%9E%84%20%EA%B0%9C%EB%B0%9C.py)  |  [code] | [code]  | [code]  |
| 럭키 스트레이트     |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/5%20-%20%EB%9F%AD%ED%82%A4%20%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%9D%B4%ED%8A%B8.py)  |  [code] | [code]  | [code]  |
| 문자열 재정렬       |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/6%20-%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%9E%AC%EC%A0%95%EB%A0%AC.py)  |  [code] | [code]  | [code]  |
| 문자열 압축        |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/7%20-%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%95%95%EC%B6%95.py)  |  [code] | [code]  | [code]  |
| 자물쇠와 열쇠       |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/8%20-%20%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80%20%EC%97%B4%EC%87%A0.py)  |  [code] | [code]  | [code]  |
| 뱀               |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/9%20-%20%EB%B1%80.py)  |  [code] | [code]  | [code]  |
| 기둥과 보 설치      |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/10%20-%20%EA%B8%B0%EB%91%A5%EA%B3%BC%20%EB%B3%B4%20%EC%84%A4%EC%B9%98.py)  |  [code] | [code]  | [code]  |
| 치킨 배달          |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/11%20-%20%EC%B9%98%ED%82%A8%20%EB%B0%B0%EB%8B%AC.py)  |  [code] | [code]  | [code]  |
| 외벽 점검         |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/12%20-%20%EC%99%B8%EB%B2%BD%20%EC%A0%90%EA%B2%80.py)  |  [code] | [code]  | [code]  |
|  달팽이             |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/%EB%8B%AC%ED%8C%BD%EC%9D%B4%201913.py)  |          |        |           |
|  달팽이2            |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/%EB%8B%AC%ED%8C%BD%EC%9D%B42%201952.py)  |          |        |           |
|  소코반             |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/2.%20Implementation/songhee/%EC%86%8C%EC%BD%94%EB%B0%98%204577.py) |          |        |           | 
