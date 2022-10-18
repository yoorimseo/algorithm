function solution(my_string) {
    var answer = my_string.replace(/[^0-9]/g, "");
    let arr = answer.split("").map(str => parseInt(str));
    return arr.sort((a, b) => a - b);
}