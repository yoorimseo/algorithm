function solution(n) {
    let answer = 1;
    let i = 1;
    let cnt = 0;
    
    while (answer <= n) {
        answer *= i;
        i++;
        cnt++;
    }
    
    return cnt - 1;
}