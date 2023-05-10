""" 
- 특정 키워드가 몇 개 포함되어 있는지 찾기
- ? 는 어떤 문자랑도 매치

** subn 사용하면 정확성에서 2case 실패하는데, sub 사용하면 통과함
"""

####################################
# Trie 자료구조 활용
####################################
class Node(object):
    def __init__(self, key, data=None):
        self.key = key      # 해당 노드의 문자
        self.data = data    # 문자열 끝나는 위치
        self.count = 0      # 문자 개수
        self.children = {}  # 자식 노드

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.count = 0
    
    def insert(self, string):
        curr_node = self.head
        self.count += 1
        
        for char in string:
            # 자식 Node 중 같은 문자 없으면 Node 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 있으면 Node로 이동
            curr_node = curr_node.children[char]
            curr_node.count += 1
            
        # 문자열 끝난 지점의 노드 data에 문자열 입력
        curr_node.data = string
    
    def search(self, string):
        # 위 노드부터 차례로 탐색
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        return curr_node.count


def solution(words, queries):
    answer = [0] * len(queries)
    trie = {}
    trie_r = {}

    # 글자 길이 수 별로 trie 만들기
    for word in words:
        if len(word) not in trie:
            trie[len(word)] = Trie()
            trie_r[len(word)] = Trie()
        
        trie[len(word)].insert(word)
        trie_r[len(word)].insert(word[::-1])

    for i, query in enumerate(queries):
        if len(query) not in trie:  # 해당 쿼리 길이의 단어 없음
            continue

        qm = query.count('?')
        if len(query) == qm:        # 쿼리가 ?로만 이루어짐
            answer[i] = trie[len(query)].count
            continue
        
        if query[0] == '?':     # 접두사가 ?
            answer[i] = trie_r[len(query)].search(query[qm:][::-1])
        else:
            answer[i] = trie[len(query)].search(query[:len(query)-qm])
    return answer


####################################
# 이진 탐색 활용
####################################

from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = [0] * len(queries)
    
    # 단어를 길이 별로 분류 & 정렬
    words_len = {}
    words_len_r = {}
    for w in words:
        n = len(w)
        if n in words_len:
            words_len[n].append(w)
            words_len_r[n].append(w[::-1])
        else:
            words_len[n] = [w]
            words_len_r[n] = [w[::-1]]

    for k in words_len:
        words_len[k].sort()
        words_len_r[k].sort()
    
    # 쿼리의 ? 를 a와 z로 변환하기
    qidx = []
    for query in queries:
        if query[0] == '?': # 접두사인 경우
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
            flag = 'r'
        else:               # 접미사인 경우
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
            flag = ''
        qidx.append((len(query), start, end, flag))
            
    # 쿼리와 일치하는 단어 개수 찾기
    for i, query in enumerate(queries):
        if qidx[i][0] not in words_len :     # 쿼리 길이에 맞는 단어가 없는 경우
            continue
        
        if qidx[i][-1] == 'r':
            word_cands = words_len_r[qidx[i][0]]
        else:
            word_cands = words_len[qidx[i][0]]
        if query.count('?') == qidx[i][0] :  # 쿼리가 ????? 인 경우
            answer[i] = len(word_cands)
            continue
        
        answer[i] = bisect_right(word_cands, qidx[i][2]) - bisect_left(word_cands, qidx[i][1])
    
    
    return answer


####################################
# re 패키지 활용
# 효율성 통과 X
####################################
"""
import re

def solution(words, queries):
    answer = [0] * len(queries)
    
    # 단어를 길이별로 분류
    words_len = {}
    for w in words:
        n = len(w)
        if n in words_len:
            words_len[n].append(w)
        else:
            words_len[n] = [w]
    
    # 쿼리 내 ? 를 [a-z]로 변환
    qn = [ len(q) for q in queries ]    # 쿼리 단어 길이
    queries_que = []
    for i, q in enumerate(queries):
        w = ''
        for i in range(qn[i]):
            if q[i] == '?':
                w += '[a-z]'
            else:
                w += q[i]
        queries_que.append(w)
    
    for i, query in enumerate(queries_que):
        if qn[i] in words_len:
            for word in words_len[qn[i]]:
                if re.sub(query, '', word) == '' :
                    answer[i] += 1
            
    return answer
"""
