'''
- sol1
    - 각 길이별로 단어를 정렬해서 cands와 reverse_cands 딕셔너리를 만든다.
    - 딕셔너리 안의 Value를 정렬한다.
    - queries를 탐색하면서, 
        - 현재 쿼리의 길이를 Key로 가지는 딕셔너리의 값(리스트)을 가져온다.
            - 접두사라면, reverse_cands
            - 접미사라면, cands
        - 접두사와 접미사를 구분해서 '?'를 'a', 'z'로 바꾼다.
            - start : '?'를 'a'로 바꾼 문자열
            - end : '?'를 'z'로 바꾼 문자열
        - bisect 모듈을 사용해서 현재 쿼리와 일치하는 단어가 몇개인지 카운트한다.
        
    e.g) query = "fro??" -> start = "froaa", end = "frozz"
        접미사이므로 cands[len(query) = 5]를 가져온다 => ["frodo", "front", "frost", "frame"]
        bisect_right - bisect_left => 위의 리스트에 "frozz" ~ "froaa" 사이에 해당하는 문자열이 있는지 개수 세는 것
    
    
-> ✅다시 풀기
'''
from collections import defaultdict
from bisect import bisect_left, bisect_right

# sol 1 
def count_by_range(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)

def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    
    # words 안의 단어들을 길이를 기준으로 딕셔너리에 저장
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
    
    # 정렬 O(NlogN)
    for cand in cands.values():
        cand.sort()
    
    for cand in reverse_cands.values():
        cand.sort()
    
    # 탐색 O(N * logM)
    for query in queries:
        
        # 접두사 
        # 비교를 쉽게 하기 위해서 쿼리를 거꾸로 
        if query[0] == '?': 
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?','z')
            
        # 접미사
        else:
            lst = cands[len(query)]
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
        
        answer.append(count_by_range(lst, start, end))
        
    return answer

# sol 2
def solution(words, queries):
    cands, reverse_cands = {}, {}
    wild_card = []
    
    def add(head, word):
        node = head
        for w in word:
            if w not in node:
                node[w] = {}
                
            node = node[w]
            
            if 'len' not in node:
                node['len'] = [len_word]
            else:
                node['len'].append(len_word)
        node['end'] = True
        
    for word in words:
        len_word = len(word)
        add(cands, word)
        add(reverse_cands, word[::-1])
        wild_card.append(len(word))
    
    def search(head, query):
        count = 0
        node = head
        
        for q in query:
            if q == '?':
                return node['len'].count(len_qu)
            elif q not in node:
                break
            node = node[q]
            
        return count
    
    lst = []
    for query in queries:
        len_qu = len(query)
        if query[0] == '?':
            if query[-1] == '?':
                lst.apend(wild_card.count(len_qu))
            else:
                lst.append(search(reverse_cands, query[::-1]))
        else:
            lst.append(search(cands, query))
            
    return lst