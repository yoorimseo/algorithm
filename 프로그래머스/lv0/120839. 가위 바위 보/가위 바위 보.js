function solution(rsp) {
    var answer = [];
    let rspArr = rsp.split("");
    
    for (i of rspArr) {
        if (i === "2") {
            answer.push("0");
        } else if (i === "0") {
            answer.push("5");
        } else if (i === "5") {
            answer.push("2");
        }
    }
    return answer.join("");
}