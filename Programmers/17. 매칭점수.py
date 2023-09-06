'''
기본점수, 외부 링크 수, 링크점수, 매칭점수
- 기본 점수 : 검색어 등장 횟수 (대소문자 구분 x, 알파벳을 제외한 모든 문자로 구분)
- 외부 링크 수 : 외부 페이지 연결 링크 개수
- 링크 점수 : (해당 웹페이지로 링크를 한 다른 페이지의 기본 점수) / 외부 링크 수
- 매칭 점수 : 기본 점수 + 링크 점수


return 매칭점수 max의 index 여러개면 작은 것

웹 페이지 url은 meta에 content에 있음
외부 링크는 <a href = 링크 >
'''

import re

def solution(word, pages):
    webpage = []
    webpageName = []
    webpageLink = dict()
    
    for page in pages:
        #웹페이지의 url 찾기
        url = re.search('<meta property="og:url" content="(\S+)"',page).group(1)
        
        #모든 검색어 찾기
        basic = 0
        for i in re.findall(r'[a-zA-Z]+', page.lower()):
            if i == word.lower():
                basic += 1
        
        #모든 외부 링크 찾기
        link = re.findall('<a href="(https://[\S]*)"', page)

        for l in link:
            if l not in webpageLink.keys():
                webpageLink[l] = [url]
            else:
                webpageLink[l].append(url)
        
        webpageName.append(url)
        webpage.append([url, basic, len(link)])
    
    maxValue = 0
    result = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        
        if url in webpageLink.keys():
            for l in webpageLink[url]:
                a, b, c = webpage[webpageName.index(l)]
                score += (b/c)
                
        if maxValue < score:
            maxValue = score
            result = i
    
    return result
