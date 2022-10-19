function solution(age) {
    let newAge = age.toString().split(""); // ["2", "3"]
    let ageList = {
        "0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h", "8": "i", "9": "j"
    }
    let answer = "";
    
    for (s of newAge) {
        answer += ageList[s];
    }
    
    return answer;
    
    return
}