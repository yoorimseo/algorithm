function solution(arr) {
    const answer = []
    
    for (let i of arr) {
        for (let j = 0; j < i; j++) {
            answer.push(i)
        }
    }
    
    return answer
}