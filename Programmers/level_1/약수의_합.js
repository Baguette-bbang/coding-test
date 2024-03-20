function solution(n) {
    var answer = 1 + n;
    if (n === 1 || n === 0) {
        return n;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            n / i === i ? answer += i : answer += i + n / i;
        }
    }
    return answer;
}