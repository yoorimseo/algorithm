function solution(n) {
    var answer = 0
    let arr = n.toString().split("");
    
    arr.forEach(num => answer += parseInt(num));
    
    return answer;
}