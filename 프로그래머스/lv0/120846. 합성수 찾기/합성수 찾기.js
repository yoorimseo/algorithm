function solution(n) {
    let answer = [];
    
    for (let i = 1; i <= n; i++) {
        const arr = [];
        for (let j = 1; j <= i; j++) {
            if (i % j === 0) {
                arr.push(j);
            }
        }
        arr.length >= 3 && answer.push(i)
    }
    
    return answer.length;
}