function solution(t, p) {
    var answer = 0;
    let intP = parseInt(p);
    for (let i = 0; i <= t.length-p.length; i++) {
        parseInt(t.substr(i, p.length)) <= intP ? answer += 1 : answer;
    } 
    return answer;
}