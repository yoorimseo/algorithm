function solution(array) {
    var answer = array.toString().split("").filter(n => n === "7");
    return answer.length;
}