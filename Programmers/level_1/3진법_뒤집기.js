function solution(n) {
    var answer = 0;
    let temp = n.toString(3);
    for (let i = 0; i < temp.length; i++) {
        answer += parseInt(temp[i]) * Math.pow(3,i)
    }
    return answer;
}