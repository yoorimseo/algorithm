function solution(numbers) {
    var answer = 0;
    numbers.forEach(function(n) {
        answer += n;
    })
    return answer / numbers.length;
}