vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input()
    if text == "end":
        break

    v_cnt = 0
    v_repeat, c_repeat = 0, 0
    last = ''
    flag = True

    for i in text:
        if i in vowel:
            if v_repeat == 2 or ((i != 'e' and i != 'o') and last == i):
                flag = False
                break
            else:
                v_repeat += 1
                c_repeat = 0
                v_cnt += 1
                last = i

        else:
            if c_repeat == 2 or last == i:
                flag = False
                break
            else:
                c_repeat += 1
                v_repeat = 0
                last = i
                
    if v_cnt == 0:
        flag = False

    if flag:
        print(f'<{text}> is acceptable.')
    else:
        print(f'<{text}> is not acceptable.')