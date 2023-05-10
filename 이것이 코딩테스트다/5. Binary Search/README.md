## Binary Search

탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘 O(logN)

- 전제 조건 : 데이터가 `'정렬'` 되어 있어야 함
- Tree 자료구조로 데이터를 저장하면 이진 탐색과 같은 기법으로 빠르게 탐색이 가능하다

<br>



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

<br>



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

<br>

<br>

### 문제

|                                         | 송희                                                         | 숙경 | 주현 | 휘식 |
| --------------------------------------- | ------------------------------------------------------------ | ---- | ---- | ---- |
| 부품 찾기                               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/01.%20%EB%B6%80%ED%92%88%20%EC%B0%BE%EA%B8%B0.py) |      |      |    [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/01.%20%EB%B6%80%ED%92%88%20%EC%B0%BE%EA%B8%B0.py)  |
| 떡볶이 떡 만들기                        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/02.%20%EB%96%A1%EB%B3%B6%EC%9D%B4%20%EB%96%A1%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py) |      |      |   [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/02.%20%EB%96%A1%EB%B3%B6%EC%9D%B4%20%EB%96%A1%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py)   |
| 정렬된 배열에서 특정 수의 개수 구하기 ❗ | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/03.%20%EC%A0%95%EB%A0%AC%EB%90%9C%20%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C%20%ED%8A%B9%EC%A0%95%20%EC%88%98%EC%9D%98%20%EA%B0%9C%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0.py) |      |      |  [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/03.%20%EC%A0%95%EB%A0%AC%EB%90%9C%20%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C%20%ED%8A%B9%EC%A0%95%20%EC%88%98%EC%9D%98%20%EA%B0%9C%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0.py)    |
| 고정점 찾기                             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/04.%20%EA%B3%A0%EC%A0%95%EC%A0%90%20%EC%B0%BE%EA%B8%B0.py) |      |      |   [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/04.%20%EA%B3%A0%EC%A0%95%EC%A0%90%20%EC%B0%BE%EA%B8%B0.py)   |
| 공유기 설치 ✅                           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/05.%20%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98.py) |      |      |   [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/05.%20%EA%B3%B5%EC%9C%A0%EA%B8%B0%20%EC%84%A4%EC%B9%98.py)   |
| 가사 검색 ✅                             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/06.%20%EA%B0%80%EC%82%AC%20%EA%B2%80%EC%83%89.py) |      |      |   [code](https://github.com/songhee-lee/2023-python-coding-test/blob/e22c8367a5124d85d762c780b668629f6d8020a1/5.%20Binary%20Search/Hwisik/06.%20%EA%B0%80%EC%82%AC%20%EA%B2%80%EC%83%89.py)   |
| 숫자 카드 2                             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/07.%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C2.py) |      |      |  [code]()    |
| 좌표 압축                               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/08.%20%EC%A2%8C%ED%91%9C%20%EC%95%95%EC%B6%95.py) |      |      |  [code]()   |
| 세 수의 합                              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/09.%20%EC%84%B8%20%EC%88%98%EC%9D%98%20%ED%95%A9.py) |      |      |   [code]()   |
| 숫자 카드                               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/10.%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C.py) |      |      |  [code]()    |
| 차집합                                  | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/11.%20%EC%B0%A8%EC%A7%91%ED%95%A9.py) |      |      |  [code]()    |
| 용액                                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/12.%20%EC%9A%A9%EC%95%A1.py) |      |      |   [code]()   |
| 좋다                                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/13.%20%EC%A2%8B%EB%8B%A4.py) |      |      |  [code]()    |
| 두 배열의 합                            | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/14.%20%EB%91%90%20%EB%B0%B0%EC%97%B4%EC%9D%98%20%ED%95%A9.py) |      |      |  [code]()    |
| 합이 0인 네 정수                        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/15.%20%ED%95%A9%EC%9D%B4%200%EC%9D%B8%20%EB%84%A4%20%EC%A0%95%EC%88%98.py) |      |      |   [code]()   |
| 가장 긴 증가하는 부분 수열2             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/16.%20%EA%B0%80%EC%9E%A5%20%EA%B8%B4%20%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B42.py) |      |      |   [code]()   |
| 예산                                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/17.%20%EC%98%88%EC%82%B0.py) |      |      |  [code]()    |
| 택배                                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/18.%ED%83%9D%EB%B0%B0.py) ✅ |      |      |   [code]()   |
| 수 찾기                                 | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/20.%20%EC%88%98%20%EC%B0%BE%EA%B8%B0.py) |      |      |  [code]()    |
| 나무 자르기                             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/21.%20%EB%82%98%EB%AC%B4%20%EC%9E%90%EB%A5%B4%EA%B8%B0.py) |      |      |   [code]()   |
| 랜선 자르기                             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/22.%20%EB%9E%9C%EC%84%A0%20%EC%9E%90%EB%A5%B4%EA%B8%B0.py) |      |      |   [code]()   |
| 카드                                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/23.%20%EC%B9%B4%EB%93%9C.py) |      |      |  [code]()    |
| 구간 나누기2                            | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/24.%20%EA%B5%AC%EA%B0%84%20%EB%82%98%EB%88%84%EA%B8%B02.py) |      |      |   [code]()   |
| 중량제한                                | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/25.%20%EC%A4%91%EB%9F%89%EC%A0%9C%ED%95%9C.py) |      |      |  [code]()    |
| 배열에서 이동                           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/26.%20%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C%20%EC%9D%B4%EB%8F%99.py) ✅ |      |      |   [code]()   |
| K번째 수                                | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/27.%20K%EB%B2%88%EC%A7%B8%20%EC%88%98.py) |      |      |   [code]()   |
| 놀이공원                                | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/28.%20%EB%86%80%EC%9D%B4%20%EA%B3%B5%EC%9B%90.py) ✅ |      |      |   [code]()   |
| 사다리                                  | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/29.%20%EC%82%AC%EB%8B%A4%EB%A6%AC.py) |      |      |  [code]()    |
| 선분과 점                               | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/5.%20Binary%20Search/songhee/30.%20%EC%84%A0%EB%B6%84%EA%B3%BC%20%EC%A0%90.py) |      |      |   [code]()   |

