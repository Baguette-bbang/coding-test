function solution(d, budget) {
    var answer = 0;
    // 정확한 금액을 지원(더 적은 금액은 지원 불가능)
    d.sort((a,b) => a - b)
    let i = 0
    while (budget >= 0) {
        budget -= d[i];
        i += 1;
        answer += 1;
    }
    return answer-1;
}