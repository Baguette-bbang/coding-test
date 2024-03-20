function solution(num) {
    var answer = -1;
    let cnt = 0;
    while (cnt < 500) {
        if (num === 1) {
            answer = cnt;
            break;
        }
        num % 2 === 0 ? num /= 2 : num = num * 3  + 1;
        cnt += 1
        
    }
    return answer;
}