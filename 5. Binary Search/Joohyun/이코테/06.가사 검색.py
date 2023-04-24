def solution(words, queries):
    head, head_rev = {}, {}
    wc = []
    
    def add(head,word):
        node = head
        for w in word:
            if w not in node:
                node[w]={}
            node= node[w]
            if 'len' not in node:
                node['len'] = [len_word]
            else:
                node['len'].append(len_word)
        node['end']=True   
    
    for word in words:
        len_word = len(word)
        add(head,word)
        add(head_rev,word[::-1])
        wc.append(len_word)
        
    def search(head, querie):
        count=0
        node = head
        for q in querie:
            if q=='?':
                return node['len'].count(len_qu)
            elif q not in node:
                break
            node = node[q]
        return count

    li=[]
    for querie in queries:
        len_qu = len(querie)
        if querie[0]=='?':
            if querie[-1]=='?': 
                li.append(wc.count(len_qu))
            else: 
                li.append(search(head_rev, querie[::-1]))
        else:
            li.append(search(head, querie))
    return li




## 시간 초과 ##
"""
def binary_search_ALL(words,query,WCcnt,cnt,start,end,visited):
        while start <= end:
            mid = (start+end)//2
            visited[mid] = False # 방문 표시
            
            # 가사 단어 자르기, 키워드와 비교
            word_len = len(words[mid])    # 가사 단어 길이
            if WCcnt == word_len :   # 키워드와 가사 단어 길이가 같은 경우
                cnt+=1
                # 좌측 리스트 확인 : 좌측 리스트의 중심점에 방문한 적 없으면 좌측 리스트로 이동
                if start != end and visited[(start+mid-1)//2] : end = mid-1
                # 우측 리스트 확인 : 우측 리스트의 중심점에 방문한 적 없으면 우측 리스트로 이동
                if start != end and visited[(mid+1+end)//2] : start = mid+1
            
            # 좌측 리스트 확인 : 키워드가 가사 단어보다 짧은 경우 순서가 더 앞인 경우
            elif WCcnt == word_len : end = mid-1
            
            # 우측 리스트 확인 : 키워드가 가사 단어보다 순서가 더 뒤인 경우
            else : start = mid+1
            
        return cnt
            
def binary_search_Left(words,query,WCcnt,alph,cnt,start,end,visited):
        while start <= end:
            mid = (start+end)//2
            visited[mid] = False # 방문 표시
            
            # 가사 단어 자르기, 키워드와 비교
            word = words[mid][WCcnt:]    # 가사 단어 자르기
            if alph == word :   # 키워드와 가사 단어와 같은 경우
                cnt+=1
                # 좌측 리스트 확인 : 좌측 리스트의 중심점에 방문한 적 없으면 좌측 리스트로 이동
                if start != end and visited[(start+mid-1)//2] : end = mid-1
                # 우측 리스트 확인 : 우측 리스트의 중심점에 방문한 적 없으면 우측 리스트로 이동
                if start != end and visited[(mid+1+end)//2] : start = mid+1
            
            # 좌측 리스트 확인 : 키워드가 가사 단어보다 순서가 더 앞인 경우
            elif alph < word : end = mid-1
            
            # 우측 리스트 확인 : 키워드가 가사 단어보다 순서가 더 뒤인 경우
            else : start = mid+1
            
        return cnt
            
def binary_search_Right(words,query,WCcnt,alph,cnt,start,end,visited):
        while start <= end:
            mid = (start+end)//2
            visited[mid] = False # 방문 표시
            
            # 가사 단어 자르기, 고정단어와 비교
            word = words[mid][:-WCcnt]    # 가사 단어 자르기
            if alph == word :
                cnt+=1
                # 좌측 리스트 확인 : 좌측 리스트의 중심점에 방문한 적 없으면 좌측 리스트로 이동
                if start != end and visited[(start+mid-1)//2] : end = mid-1
                # 우측 리스트 확인 : 우측 리스트의 중심점에 방문한 적 없으면 우측 리스트로 이동
                if start != end and visited[(mid+1+end)//2] : start = mid+1
            # 좌측 리스트 확인 : 키워드가 가사 단어보다 순서가 더 앞인 경우
            elif alph < word : end = mid-1
            # 우측 리스트 확인 : 키워드가 가사 단어보다 순서가 더 뒤인 경우
            else : start = mid+1
        return cnt
    
def solution(words, queries):
    # 가사에 사용된 단어 정렬
    words.sort()
    answer = []
    words_len = len(words)
    for query in queries:
        # 방문 여부 확인
        visited = [True for _ in range(words_len)]
        # 와일드카드 개수
        WCcnt = query.count('?')
        
        # 와일드 카드 위치 : 전체 / 접두사 / 접미사
        if words_len == WCcnt :  # 전체에 와일드 카드
            words.sort(key=lambda x:len(x))
            answer.append(binary_serach_ALL(words,query,WCcnt,0,0,words_len-1,visited))
            words.sort()
        elif query.find('?')==0 : # 접두사에 와일드카드
            answer.append(binary_search_Left(words,query,WCcnt,query[WCcnt:],0,0,words_len-1,visited))
        else :                  # 접미사에 와일드카드
            answer.append(binary_search_Right(words,query,WCcnt,query[:-WCcnt],0,0,words_len-1,visited))
        
    return answer
"""