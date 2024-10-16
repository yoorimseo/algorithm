function solution(arr, k) {    
    if (k % 2 === 0) {
        return arr.map(i => i + k);
    } else {
        return arr.map(i => i * k);
    }
}