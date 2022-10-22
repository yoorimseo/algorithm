function solution(my_string, num1, num2) {
    let arr = my_string.split("");
    const change = arr.splice(num1, 1, arr[num2]).join("");
    arr.splice(num2, 1, change);

    return arr.join("");
}