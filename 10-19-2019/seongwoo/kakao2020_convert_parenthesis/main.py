def is_it_right_parenthesis(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return stack == []


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '':
        return ''

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    open_count = 0
    close_count = 0
    i = 0
    for i, char in enumerate(p):
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            break
    u, v = p[0:i+1], p[i+1:len(p)]
    if is_it_right_parenthesis(u):
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    else:
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        # 4-5. 생성된 문자열을 반환합니다.
        return '(' + solution(v) + ')' + ''.join([')' if char == '(' else '(' for char in u[1:-1]])
