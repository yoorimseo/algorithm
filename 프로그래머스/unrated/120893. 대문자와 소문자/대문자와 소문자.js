function solution(my_string) {
    var answer = '';
    for (i of my_string) {
        if ((/[a-z]/g).test(i)) {
            answer += i.toUpperCase();
        } else if ((/[A-Z]/g).test(i)) {
            answer += i.toLowerCase()
        }
    }
    return answer;
}