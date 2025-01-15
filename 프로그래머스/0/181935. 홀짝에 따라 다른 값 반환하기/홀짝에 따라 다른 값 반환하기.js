function solution(n) {
    var answer = 0
    const arr = [...new Array(n)].map((_, i) => i+1)
    
    if (n % 2 == 0) {
        answer = arr.filter(i => i % 2 == 0)
                    .map(i => Math.pow(i, 2))
                    .reduce((acc, cur) => acc + cur, 0)
    } else {
        answer = arr.filter(i => i % 2 == 1)
                    .reduce((acc, cur) => acc + cur, 0)
    }
    
    return answer
}