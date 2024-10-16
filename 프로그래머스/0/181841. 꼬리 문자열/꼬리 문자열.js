function solution(str_list, ex) {
    let answer = ''
    
    for (s of str_list) {
        if (!s.includes(ex)) {
            answer += s
        }
    }
    
    return answer
}