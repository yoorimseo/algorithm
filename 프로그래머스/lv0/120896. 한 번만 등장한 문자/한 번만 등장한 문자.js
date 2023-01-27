function solution(s) {
    let obj = {};
    let answer = '';
    
    for (let i of s) {
        if (!obj[i]) {
            obj[i] = 1;
        } else {
            obj[i] += 1;
        }
    }
        
    for (let i in obj) {
        if (obj[i] === 1) {
            answer += i;
        }
    }
    
    return answer.length === 0 ? '' : answer.split('').sort().join('');
}