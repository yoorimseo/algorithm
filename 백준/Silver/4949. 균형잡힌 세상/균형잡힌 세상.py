while True:
    string = input()

    if string == '.':
        break
        
    stack = []

    for i in string:
        if stack:
            cmp = stack.pop()

            if (i == ')' and cmp == '(') or (i == ']' and cmp == '['):
                continue
            else:
                stack.append(cmp)

                if i in ('(', '[', ')', ']'):
                    stack.append(i)
        else:
            if i in ('(', '[', ')', ']'):
                stack.append(i)

    if stack:
        print('no')
    else:
        print('yes')