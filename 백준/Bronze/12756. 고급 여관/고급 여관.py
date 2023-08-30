A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

while True:
    A2 -= B1
    B2 -= A1
    
    if A2 <= 0 and B2 <= 0:
        print('DRAW')
        break
    elif B2 <= 0:
        print('PLAYER A')
        break
    elif A2 <= 0:
        print('PLAYER B')
        break