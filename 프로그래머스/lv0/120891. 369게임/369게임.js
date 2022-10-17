function solution(order) {
    var answer = order.toString()
        .split("").filter(n => n === "3" || n === "6" || n === "9");
    return answer.length;
}