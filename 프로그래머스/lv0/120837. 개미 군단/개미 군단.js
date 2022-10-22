function solution(hp) {
    const generalAnt = Math.floor(hp / 5);
    const soldierAnt = Math.floor((hp - generalAnt * 5) / 3);
    const workerAnt = Math.floor(hp - (generalAnt * 5 + soldierAnt * 3) / 1);
    
    return generalAnt + soldierAnt + workerAnt;
}