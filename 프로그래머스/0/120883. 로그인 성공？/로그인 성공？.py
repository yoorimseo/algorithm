def solution(id_pw, db):
    login = 0
    fail = 0
    worng_pw = 0

    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                login += 1
            else:
                worng_pw += 1
        else:
            fail += 1

    if login:
        return 'login'
    elif worng_pw:
        return 'wrong pw'
    else:
        return 'fail'