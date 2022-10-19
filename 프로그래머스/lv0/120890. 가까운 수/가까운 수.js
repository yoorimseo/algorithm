function solution(array, n) {
    let assendingOrder = array.sort((a, b) => a - b);
    let minNum = Math.min(...assendingOrder.map(num => Math.abs(num - n)));

    return assendingOrder.find(num => Math.abs(num - n) === minNum);
}