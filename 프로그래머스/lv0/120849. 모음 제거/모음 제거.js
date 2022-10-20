function solution(my_string) {
    if(my_string.includes(" ")) {
        let res = my_string.split(" ").map(str => str.replace(/(a|e|i|o|u)/g, ""));
        return res.join(" ");

    } else {
        return my_string.replace(/(a|e|i|o|u)/g, "");
    }
}