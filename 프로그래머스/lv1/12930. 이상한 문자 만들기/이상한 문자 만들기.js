function solution(s) {
    const arr = s.split(' ');
    let answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        let str = arr[i].split('');
        let res = '';
        
        for (let j in str) {
            if (j % 2 === 0) {
                res += str[j].toUpperCase();
            } else {
                res += str[j].toLowerCase();
            }
        }
        
        answer.push(res);
    }
    
    return answer.join(' ');
}