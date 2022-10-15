function solution(dot) {
    if (dot[0] * dot[1] > 0) {
        if (dot[0] < 0) {
            return 3;
        }
        return 1;
    } else {
        if (dot[0] > 0) {
            return 4;
        }
        return 2;
    }
}