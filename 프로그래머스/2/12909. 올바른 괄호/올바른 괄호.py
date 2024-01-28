def solution(s): ### ()))((
    num = 0
    if s[0] == ")":
        return False
        
    for i in s:
        if i == "(":
            num += 1
        else: 
            if num == 0:
                return False
            else:
                num -= 1
    if num == 0:
        return True
    else:
        return False