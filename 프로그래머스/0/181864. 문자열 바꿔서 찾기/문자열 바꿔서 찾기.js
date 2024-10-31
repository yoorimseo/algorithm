function solution(myString, pat) {
    let newString = ''
    
    for (let i of myString) {
        if (i === 'A') {
            newString += 'B'
        } else {
            newString += 'A'
        }
    }
    
    return newString.includes(pat) ? 1 : 0
}