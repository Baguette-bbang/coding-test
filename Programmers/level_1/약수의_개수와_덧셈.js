function solution(left, right) {
    let answer = 0;
    // 약수의 개수를 구하기
    // 약수의 개수가 홀수 인지 짝수인지 체크하기
    function factorsNum(number) {
        if (number == 1) {
            return 1;
        }
        let result = 2;
        for(let i = 2; i <= Math.sqrt(number); i++) {
            if (number%i == 0) {
                i*i == number ? result += 1 : result += 2;
            }
        }
        return result;
    }
    
    for (let i = left; i <= right; i++) {
        const cnt = factorsNum(i)
        if (cnt%2 == 0) {
            answer += i;
        } else {
            answer -= i;
        }
    }
    return answer;
}