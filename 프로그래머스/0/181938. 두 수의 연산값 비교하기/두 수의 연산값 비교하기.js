function solution(a, b) {
    let res1 = Number(String(a) + String(b));
    let res2 = 2 * a * b;
    
    return Math.max(res1, res2);
}