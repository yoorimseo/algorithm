function solution(num_str) {
    const answer = num_str.split('')
                          .map(i => Number(i))
                          .reduce((acc, cur) => acc + cur, 0)
    
    return answer
}