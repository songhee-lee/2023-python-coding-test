def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == '':
        return ''

    # 2. 균형잡힌 괄호 문자열 u, v로 분리하기
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    # 3. 올바른 괄호문자열인지 판단
    def is_correct(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()
        return True

    # 4. 올바른 괄호 문자열로 바꾸기
    if is_correct(u):
        return u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = u[1:-1]
        for c in u:
            if c == '(':
                temp += ')'
            else:
                temp += '('
        return temp
