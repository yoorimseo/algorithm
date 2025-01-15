function solution(str_list, ex) {
    const answer = str_list.filter(i => !(i.includes(ex)))
    return answer.join('')
}