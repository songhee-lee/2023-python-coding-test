def solution(n, k, cmd):
    cur = k  # 현재 커서 위치
    deleted = []  # 삭제된 원소들을 저장하는 리스트
    table = {i: [i - 1, i + 1] for i in range(n)}  # 인덱스 간의 연결 정보를 저장하는 딕셔너리
    answer = ['O'] * n  # 원소 상태를 저장하는 리스트

    for c in cmd:
        if c[0] == "C":  # 삭제
            deleted.append([cur, answer[cur]])  # 삭제된 원소의 위치와 상태를 저장
            answer[cur] = 'X'  # 원소 상태를 'X'로 변경
            prev, nxt = table[cur]  # 이전 원소와 다음 원소의 인덱스
            if prev != -1:
                table[prev][1] = nxt  # 이전 원소의 다음 원소를 다음 원소로 변경
            if nxt != n:
                table[nxt][0] = prev  # 다음 원소의 이전 원소를 이전 원소로 변경
            if nxt == n:
                cur = prev  # 마지막 원소를 삭제한 경우, 커서를 이전 원소로 이동
            else:
                cur = nxt  # 다음 원소를 삭제한 경우, 커서를 다음 원소로 이동

        elif c[0] == "Z":  # 복구
            restore, status = deleted.pop()  # 삭제된 원소를 꺼내와서 위치와 상태를 복구
            answer[restore] = status  # 원소 상태를 복구
            prev, nxt = table[restore]  # 이전 원소와 다음 원소의 인덱스
            if prev != -1:
                table[prev][1] = restore  # 이전 원소의 다음 원소를 복구된 원소로 변경
            if nxt != n:
                table[nxt][0] = restore  # 다음 원소의 이전 원소를 복구된 원소로 변경

        else:  # 커서 이동
            direction, count = c.split(' ')
            count = int(count)
            if direction == 'D':  # 아래로 이동
                for _ in range(count):
                    cur = table[cur][1]  # 다음 원소로 커서 이동
            else:  # 위로 이동
                for _ in range(count):
                    cur = table[cur][0]  # 이전 원소로 커서 이동

    return ''.join(answer)  # 결과 반환