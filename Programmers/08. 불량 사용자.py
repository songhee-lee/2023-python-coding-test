from itertools import combinations, permutations

def solution(user_id, banned_id):
    answer = 0
    def check_is_banned(user):
        for banned in banned_id:
            check = True
            if len(user) != len(banned):
                continue
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    check = False
                    break
            if check:
                return True
            
        return False
    
    user_combinations = combinations(user_id, len(banned_id))
    
    banned_list = []
    for user_combination in list(user_combinations):
        result = all([check_is_banned(user) for user in user_combination])
        if result:
            users = set(user_combination)
            if users not in banned_list:
                banned_list.append(users)
            
    return len(banned_list)