function solution(arr, n) {
    // arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열
    // arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열    
    if (arr.length % 2 == 0) {
        return arr.map((el, idx) => idx % 2 ? el + n : el)
    }
    return arr.map((el, idx) => idx % 2 ? el : el + n)
}