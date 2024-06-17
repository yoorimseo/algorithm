def solution(brown, yellow):
    for height in range(1, yellow + 1):
        if yellow % height == 0:
            width = yellow // height
            if 2 * (width + height) + 4 == brown:
                return [width + 2, height + 2]