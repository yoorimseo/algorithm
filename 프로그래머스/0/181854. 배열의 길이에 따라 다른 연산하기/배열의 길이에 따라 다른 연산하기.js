function solve(i, arr, n) {
    const answer =  arr.map((item, idx) => {
            return idx % 2 === i ? item + n : item
        })
    
    return answer
}

function solution(arr, n) {    
    if (arr.length % 2 === 0) {
        return solve(1, arr, n)
    }
    
    return solve(0, arr, n)
}