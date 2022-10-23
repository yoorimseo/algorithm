function solution(numbers) {
    numbers.sort((a, b) => a - b);

    if(numbers[0] < 0 && numbers[1] < 0) {
        return Math.max(numbers[0] * numbers[1], numbers[numbers.length - 2] * numbers[numbers.length - 1]);
    } else {
        return numbers[numbers.length - 2] * numbers[numbers.length - 1];
    }
}