## Binary Search

탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘 O(logN)

- 전제 조건 : 데이터가 `'정렬'` 되어 있어야 함
- Tree 자료구조로 데이터를 저장하면 이진 탐색과 같은 기법으로 빠르게 탐색이 가능하다

### 재귀 함수로 구현

```python
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 변환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
```

### 반복문 구현

```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+mid) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None
```

### 트라이 구조

```python
#삽입과 검색 구현
class Trie(object):
    def __init__(self):
        self.head = Node(None)
  # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 생성
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
    # 문자열이 존재하는지 search
    def search(self, string):
        #가장 아래 노드에서 부터 탐색
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        #탐색이 끝난 후 해당 노드의 data값이 존재한다면 문자 포함임
        if curr_node.data != None:
            return True
```

특징

- 문자열 특화 자료구조, 문자열을 빠르게 탐색할 수 있는 자료구조
- 공간복잡도가 커서 자주 사용하는 것은 어려움

언제 사용

- 문자열을 검색하는 문제
