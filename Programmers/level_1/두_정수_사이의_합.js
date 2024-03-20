function solution(a, b) {
    var answer = 0;
    const temp_a = Math.min(a,b)
    const temp_b = Math.max(a,b)
    for (let i = temp_a; i <= temp_b; i++) {
        answer += i;
    }
    return answer;
}