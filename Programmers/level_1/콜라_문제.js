function solution(a, b, n) {
    var answer = 0;
    let temp = 0;
    while (n >= a) {
        answer += parseInt(n/a)*b; 
        temp = parseInt(n/a) * b; // 빈 병을 주고 받을 수 있는 개수
        n -= parseInt(n/a) * a;
        n += temp;
    }
    return answer;
}