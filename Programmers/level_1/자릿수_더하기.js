function solution(n) {
    var answer = 0;
    String(n).split('').forEach((a) => answer += parseInt(a))
    return answer;
}