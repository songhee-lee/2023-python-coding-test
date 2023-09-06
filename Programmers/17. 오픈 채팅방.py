"""
- 채팅방에 누군가 들어오거나 나갈 때 메세지가 출력된다.
- 닉네임을 변경하면 기존 채팅방에 출력되어 있던 메세지의 닉네임도 전부 변경된다.
- 중복 닉네임을 허용한다. (개별 관리 필요함)
- 관리자가 보게 될 메세지를 문자열 배열 형태로 리턴하기

- 1 <= record <= 100,000
"""

from collections import defaultdict

def solution(records):
    nick_name = defaultdict(str)            # nick_name = { 유저 아이디 : 유저 닉네임}
    m = ["님이 나갔습니다.", "님이 들어왔습니다."]  # 고정 출력 메세지
    logs = []                               # 관리자가 보게 될 전체 메세지 로그 
    
    for record in records :
        cmd = record.split()

        # 닉네임 변경
        if cmd[0] == 'Change' :
            nick_name[cmd[1]] = cmd[2]
        # 들어오기 / 나가기
        else:
            x = 1 if cmd[0] == 'Enter' else 0
            logs.append((cmd[1], m[x]))
            
            if x : # 들어오는 경우 닉네임 추가
                nick_name[cmd[1]] = cmd[2]   
    
    # 관리자가 보게 될 전체 메세지 로그 완성하기
    for i in range(len(logs)) :
        uid, message = logs[i]
        logs[i] = nick_name[uid]+message
    
    return logs