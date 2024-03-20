function solution(n) {
    var answer = '';
    for (let c of String(n).split('').sort((a,b)=> b-a)) {
        answer += c
    }
    return parseInt(answer);
}