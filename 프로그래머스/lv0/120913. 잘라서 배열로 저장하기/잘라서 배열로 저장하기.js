function solution(my_str, n) {
    var answer = [];
    let num = Math.ceil(my_str.length / n);
    
    for(let i = 0; i < num; i++) {
        let newStr = my_str.split("").splice(i * n, n).join("");
        answer.push(newStr);
    }
    return answer;
}