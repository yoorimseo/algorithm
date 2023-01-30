function solution(balls, share) {
    let num1 = 1;
    let num2 = 1;
    let i = 0;
    
    while (i < share) {
        num1 *= balls - i;
        num2 *= share - i;
        i++;
    }
    return num1 / num2;
}