function solution(my_string) {
    var num = my_string.replace(/[^0-9]/g, "").split("");
    let result = num.reduce((acc, cur, idx) => { return acc += parseInt(cur); }, 0);
    return result;
}