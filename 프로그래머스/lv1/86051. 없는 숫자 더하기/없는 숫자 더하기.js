function solution(numbers) {
    const numArr = numbers.map(i => Number(i)).sort((a, b) => a - b);
    let answer = [];
    
    for (let i = 0; i <= 9; i++) {
        if (!numArr.includes(i)) {
            answer.push(i);
        }
    }
    
    return answer.reduce((acc, cur) => acc + cur, 0);
}