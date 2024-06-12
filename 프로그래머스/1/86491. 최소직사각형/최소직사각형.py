def solution(sizes):
    w, h = 0, 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > w:
            w = sizes[i][0]
        if sizes[i][1] > h:
            h = sizes[i][1]
    
    return w * h