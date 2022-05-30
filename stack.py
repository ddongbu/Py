priority = {'*':3,'/':3,'+':2,'-':2,'(':1}

for t in range(1,11):
    N = int(input())
    tokens =list(map(str,input().rstrip()))     # 입력받기
    lst = []        # 빈 리스트 생성
    stack = []      # 스택 생성
    prior = {'*':3,'/':3,'+':2,'-':2,'(':1}     # 우선순위 설정
    for n in range(len(tokens)):    # 토큰의 길이만큼 반복하여
        if tokens[n].isdigit(): # 만약 숫자이면 바로 lst에 추가
            lst.append(tokens[n])
        elif tokens[n] == '(':  # (이면 바로 stack에 추가
                stack.append(tokens[n])
        elif tokens[n] == ')':  # )가 나오면 stack에서 (가 나올때까지 pop처리 및 lst에 추가.
            while stack[-1] != '(':
                lst.append(stack.pop())
            stack.pop() # (가 나타나면 pop처리
        else:   # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
            while stack and prior[tokens[n]] <= prior[stack[-1]]:
                lst.append(stack.pop()) # pop한것들은 lst에 추가 시켜줌
            stack.append(tokens[n]) # 위의 조건이 완료 되면 stack에 추가

    while len(stack) != 0:  # stack에 남아있는 연산자들 lst에 추가
        lst.append(stack.pop())

        op_check = ['+', '/', '*', '-']  # 연산자 체크를 위해 미리 생성
        stack = []  # 피연산자 바로 추가할 리스트 생성
        a1 = 0  # stack[-1]을 위한 변수 생성
        a2 = 0  # stack[-2]을 위한 변수 생성
        for l in range(len(lst)):  # 후위표기법으로 저장되 있는 리스트의 수만큼 반복
            if lst[l].isdigit():  # 만약 피연산자이면 바로 stack에 추가
                stack.append(int(lst[l]))
            elif lst[l] == '+':  # + 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 + a2)
            elif lst[l] == '-':  # - 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 - a2)
            elif lst[l] == '*':  # * 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 * a2)
            elif lst[l] == '/':  # / 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 / a2)

#후위표현식을 왼쪽부터 한글자씩 읽는다.
#피연산자이면 stack에 추가를 해준다
#연산자이면 stack[-1]과 stack[-2]를 pop해준뒤 해당 연산자로 계산을 해준다.
