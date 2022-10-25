function solution(num_list, n) {
    var answer = [];
    
    let i = 0;
    let newN = n;

    while (newN <= num_list.length) {
        answer.push(num_list.slice(i, newN));
        i += n;
        newN += n;
    }
    
    return answer;
}