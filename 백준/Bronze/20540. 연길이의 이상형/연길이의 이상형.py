mbti = input()
res = ''

res += 'I' if mbti[0] == 'E' else 'E'
res += 'N' if mbti[1] == 'S' else 'S'
res += 'F' if mbti[2] == 'T' else 'T'
res += 'P' if mbti[3] == 'J' else 'J'

print(res)