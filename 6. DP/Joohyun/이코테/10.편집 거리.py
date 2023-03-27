"""
<< 편집 action >>
1. ins : 특정 위치에 문자 1개 삽입
2. rm : 특정 위치의 문자 1개 제거
3. rpl : 특정 위치의 문자 1개를 다른 문자로 교체
"""

# 답지 참고

def edit_dist(str1,str2):
    n=len(str1)
    m=len(str2)

    d = [[0]*(m+1) for _ in range(n+1)]

    # dp 테이블 초기 설정
    for i in range(1,n+1): d[i][0] = i
    for j in range(1,m+1): d[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1,n+1):
        for j in range(1,m+1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
                if str1[i-1]==str2[i-1]: d[i][j]=d[i-1][j-1]
                # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
                else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                     d[i][j] = 1 + min(d[i][j-1],d[i-1[j],d[i-1][j-1]])
    
    return d[n][m]