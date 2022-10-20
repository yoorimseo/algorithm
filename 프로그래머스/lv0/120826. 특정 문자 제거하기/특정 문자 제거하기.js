function solution(my_string, letter) {
    var answer = my_string.split("").filter(str => str !== letter)
    return answer.join("");
}