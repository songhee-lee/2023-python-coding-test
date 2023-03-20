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