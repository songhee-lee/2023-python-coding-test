[1. re 정규 표현식](#re-정규-표현식)

[2.bisect](#bisect)

[3.Counter](#Counter)

​	[3-1 가장 흔한 데이터 찾기](#가장-흔한-데이터-찾기)



---



### re 정규 표현식

#### 문자열 뒤집기 [[code]](https://github.com/songhee-lee/2023-python-coding-test/blob/main/1.%20Greedy/Joohyun/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
```python
import re

S = input()
S = re.sub('[0]{1,}','0',S)   # 000..0 을 0으로
S = re.sub('[1]{1,}','1',S)   # 111..1 을 1로
```

<br><br>

### bisect
[[참고]](https://docs.python.org/ko/3/library/bisect.html)

- 이진 탐색을 쉽게 구현할 수 있는 라이브러리
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적
- 시간 복잡도 : O(logN)
#### 제공 함수
[ 삽입할 index 반환 ]
- bisect.bisect_left
- bisect.bisect_right
- bisect.bisect

[ 삽입 ]
- bisect.insort_left
- bisect.insort_right
- bisect.insort

#### BISECT ( listA , x , lo=0 , hi=len(listA) , * , key=None )
- 정렬된 리스트 listA에서 원소 x를 정렬 기준에 맞게 삽입할 위치(idx)를 반환한다
- bisect.bisect_left
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- bisect.bisect_right
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- bisect.bisect
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- lo, hi : 리스트의 부분 집합을 지정할 수 있다


#### INSORT ( listA , x , lo=0 , hi=len(listA) , * , key=None )
- 정렬된 리스트 listA에서 원소 x를 정렬 기준에 맞게 삽입한다
- bisect.insort_left
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스에 삽입하는 메서드
- bisect.insort_right
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스에 삽입하는 메서드
- bisect.insort
    정렬된 순서를 유지하면서 listA에 데이터 x를 삽입할 가장 오른쪽 인덱스에 삽입하는 메서드
- lo, hi : 리스트의 부분 집합을 지정할 수 있다

#### 가사 검색하기 [[code]](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/Hwisik/06.%20%EA%B0%80%EC%82%AC%20%EA%B2%80%EC%83%89.py)
```python
import bisect
temp = [1, 3, 4, 5]

print(bisect.bisect_left(temp,2)) # 1
print(temp)                  # [ 1,3,4,5 ]
print(bisect.insort_left(temp,2)) # None
print(temp)                  # [ 1,2,3,4,5 ]
```

<br><br>

## Counter

```python
from collections import Counter

# 리스트를 인자로 넘기면 각 원소가 몇 번씩 나오는지 저장된 객체 반환
>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})

# 문자열을 인자로 넘기면 각 문자가 몇 번씩 나오는지 저장된 객체 반환
>>> Counter("hello world")
Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

```python
# 사전처럼 사용 가능
counter = Counter("hello world")
>>> counter["o"], counter["l"]
(2, 3)

# 산술 연산자 활용 가능
counter1 = Counter(["A", "A", "B"])
counter2 = Counter(["A", "B", "B"])

>>> counter1 + counter2
Counter({'A': 3, 'B': 3})

>>> counter1 - counter2
Counter({'A': 1})
```

<br>

### 가장 흔한 데이터 찾기

```python
# 데이터 개수가 많은 순으로 정렬된 배열 리턴
>>> Counter('hello world').most_common()
[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
```



