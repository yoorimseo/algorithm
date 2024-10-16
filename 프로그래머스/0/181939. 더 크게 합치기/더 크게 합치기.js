function typeChange(a, b) {
    return(Number(String(a) + String(b)))
}

function solution(a, b) {
    let res1 = typeChange(a, b)
    let res2 = typeChange(b, a)
    
    return Math.max(res1, res2)
}