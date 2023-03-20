'''

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
    
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
    
    for cand in cands.values():
        cand.sort()
    
    for cand in reverse_cands.values():
        cand.sort()
    
    for query in queries:
        if query[0] == '?':
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?','z')
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