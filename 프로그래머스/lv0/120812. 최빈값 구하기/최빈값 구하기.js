function solution(array) {
    const obj = {};
    let answer = [];
    
    for (let i of array) {
        if (!obj[i]) {
            obj[i] = 1;
        } else {
            obj[i] += 1;
        }
    }
    
    const max = Math.max(...Object.values(obj));
        
    for (let i in obj) {
        if (obj[i] === max) {
            answer.push(i);
        }
    }
    
    return answer.length > 1 ? -1 : parseInt(answer[0]);
}