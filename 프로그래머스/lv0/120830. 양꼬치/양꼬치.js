function solution(n, k) {
    k = k - (Math.floor(n / 10));
    var answer = (n * 12000) + (k * 2000);
    return answer;
}