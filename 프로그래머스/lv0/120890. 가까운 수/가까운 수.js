function solution(array, n) {
    let minNum = Math.min(...array.map(num => Math.abs(num - n)));
    let assendingOrder = array.sort((a, b) => a - b);

    return assendingOrder.find(num => Math.abs(num - n) === minNum);
}