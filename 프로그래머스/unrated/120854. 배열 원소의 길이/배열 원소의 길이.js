function solution(strlist) {
    var answer = [];
    strlist.forEach(function(str) {
        answer.push(str.length);
    })
    return answer;
}