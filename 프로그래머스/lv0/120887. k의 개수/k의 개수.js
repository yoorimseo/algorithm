function solution(i, j, k) {
    let str = '';
    
    for (let num = i; num <= j; num++) {
        str += num;
    }
        
    return str.length - str.split(k).join('').length;
    
}