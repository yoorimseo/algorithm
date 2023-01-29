function solution(s) {
    const arr = s.split(' ');
    let answer = 0;
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 'Z') {
            answer -= parseInt(arr[i - 1]);
        } else {
            answer += parseInt(arr[i]);
        }
    }
    
    return answer;
}