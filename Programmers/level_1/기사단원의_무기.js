function solution(number, limit, power) {
    var answer = 1; // 1 예외처리 자기자신만을 약수로서 가짐.
    for (let i = 2; i <= number; i++) {
        let divisorCnt = 2; // 자기자신과 1은 포함된 상태임.
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                i / j === j ? divisorCnt+=1 : divisorCnt+=2;
            } 
            if (divisorCnt > limit) {
                divisorCnt = power;
                break;
            }
        }
        answer += divisorCnt;
        
    }
    return answer;
}