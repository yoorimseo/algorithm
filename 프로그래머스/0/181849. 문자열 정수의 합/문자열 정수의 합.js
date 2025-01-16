function solution(num_str) {
    let answer = num_str
                .split('')
                .map(i => parseInt(i))
                .reduce((acc, cur) => acc + cur, 0)
    
    return answer
}