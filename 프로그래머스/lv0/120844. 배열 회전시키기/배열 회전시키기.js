function solution(numbers, direction) {
    var answer = new Array(numbers.length);
    
    if(direction === "right") {
        for (let i = 1; i < numbers.length; i++) {
            answer[i] = numbers[i - 1];
            if(i === numbers.length - 1) {
                answer[0] = numbers[i];
            }
        }   
    } else {
        for(let i = 0; i < numbers.length; i++) {
            answer[i] = numbers[i + 1];
            if(i === numbers.length - 1) {
                answer[numbers.length - 1] = numbers[0];
            }
        }
    }
    return answer;
}