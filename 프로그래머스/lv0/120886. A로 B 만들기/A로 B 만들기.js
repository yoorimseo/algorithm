function solution(before, after) {
    const afterStr = after.split('');
    const beforeStr = before.split('');
    const answer = new Array(after.length);
    
    for (let s of beforeStr) {
        if (afterStr.includes(s)) {
            answer[afterStr.indexOf(s)] = s;
            afterStr[afterStr.indexOf(s)] = ' ';
        }
    }
    
    return answer.join('') === after ? 1 : 0;
}