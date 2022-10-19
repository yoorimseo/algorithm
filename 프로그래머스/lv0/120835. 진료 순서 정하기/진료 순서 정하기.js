function solution(emergency) {
    let newArr = emergency.map(n => n).sort((a, b) => b - a);
    let answer = [];
    
    for (let i = 0; i < emergency.length; i++) {
        answer.push(newArr.indexOf(emergency[i]) + 1);
    }
    
    return answer;
}