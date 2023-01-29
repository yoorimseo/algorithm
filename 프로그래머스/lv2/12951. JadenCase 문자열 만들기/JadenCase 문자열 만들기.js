function solution(s) {
    const str = s.toLowerCase().split(' ');
    let answer = [];
    
    for (let s of str) {
        const arr = s.split('');
        let word = '';
        for (let i = 0; i < arr.length; i++) {
            if (i === 0) {
                word += arr[i].toUpperCase();
            } else {
                word += arr[i];
            }
        }
        answer.push(word);
    }
    return answer.join(' ');
}