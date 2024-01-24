def solution(keyinput, board):
    x = y = 0
    limitX = (board[0] - 1) // 2
    limitY = (board[1] - 1) // 2

    for key in keyinput:
        if key == "up" and y < limitY:
            y += 1
        elif key == "down" and y > -limitY:
            y -= 1
        elif key == "right" and x < limitX:
            x += 1
        elif key == "left" and x > -limitX:
            x -= 1

    return [x, y]