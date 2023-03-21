# Trie(트라이) 자료구조
## Trie란?
문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조

> 빠른 시간복잡도를 가지고 있기 때문에, 자동 완성 및 검색어 추천 기능 등 문자열을 탐색하는 곳에서 사용한다.

## 구조
### 다음 단어들을 Trie 구조로 ["frodo", "front", "kakao", "kaggle"]
[pic]
[pic]
### 다른 예시
[pic]

 - Key는 특정 알파벳을 의미한다.
 - Data는 해당 단어가 끝남을 의미한다.
 - Child는 현재 Key에 연결된 자식 노드를 의미한다.

## 특징

 - Trie 자료구조는 노드를 이용한 Tree 형태로 이루어져 있다.
 - 문자열의 끝을 알리는 Flag가 존재한다.
## 장점&단점
### 장점
 - 문자열 검색을 빠르게 한다.
 - 문자열을 탐색할 때, 일일히 비교하는 것보다 시간복잡도 측면에서 훨씬 효율적이다.
### 단점
 - 각 노드에서 자식들에 대한 포인터들을 모두 배열로 저장하고 있어서 공간복잡도가 크다.
 ---
## 트라이(Trie) 구현 in Python
### 1. Node 클래스 생성하기
```python
    class Node(object): 
	    def __init__(self, key, data=None): 
		    self.key = key 
		    self.data = data 
		    self.children = {}
```
### 2. Dictionary 자료형을 이용하여 Trie(트라이) 구현하기
```python
    class Trie(object): 
	    def __init__(self): 
		    self.head = Node(None) 
		def insert(self, string): 
			cur_node = self.head 
			for ch in string: 
				if char not in cur_node.children: 	
					cur_node.children[ch] = Node(ch) 
				cur_node = cur_node.children[ch] 
			cur_node.data = string 
		def search(self, string): 
			cur_node = self.head 
			for ch in string: 
				if ch in cur_node.children: 
					cur_node = cur_node.children[ch] 
				else: 
					return False 
			if cur_node.data is not None: 
				return True
```
---
## 시간복잡도
> L : 제일 긴 문자열의 길이
> M : 총 문자열의 수
#### 생성 시간 복잡도 : O(ML)
#### 탐색 시간 복잡도 : O(L)

## 또 다른 구현 코드
### 저장 코드
```python
    head = {} 
    def add(word): 
	    node = head 
	    for w in word: 
		    if w not in node: 
			    node[w]={} 
			node = node[w] 
		node['end'] = True
```
‘ab’라는 문자열을 Trie 구조로 데이터를 넣는다면,

> 1.  ‘ab’를 for문을 통해서 순회한다.
> 2.  node에 ‘a’라는 Key가 존재하지 않는다면 ‘a’라는 Key를 가진 딕셔너리를 만든다.
> 3.  node[’a’] 딕셔너리의 메모리주소를 node에 넘긴다.
> 4.  node[’a’]에 ‘b’라는 Key가 존재하지 않는다면, ‘b’라는 Key를 가진 딕셔너리를 만든다.
> 5.  그리고 node[’a’][’b’]의 딕셔너리 메모리주소를 node에 넘긴다.
> 6.  모든 문자를 넣었다면 for문을 종료한다.
> 7.  해당 문자열이 끝났다는 표시로 node[’end’] = True를 넣는다.

> 😅 head와 node의 메모리 공유에 대해 공부 필요

### 찾는 코드
```python
    def search(word): 
	    node = head 
	    for w in word: 
		    if w not in node: 
			    return False 
			node = node[w] 
		if 'end' in node: 
			return True 
		else: 
			return False
```
