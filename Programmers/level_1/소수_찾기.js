function solution(n) {
    var answer = 0;
    
    // 에라토스테네스의 체 : 특정 수가 소수가 아니라면 그 수의 배수도 소수가 아님.
    let primeArray = new Array(n + 1).fill(true); // 모든 숫자를 소수라고 가정
    primeArray[0] = primeArray[1] = false; // 0과 1은 소수가 아님
    
    function check_prime(num) {
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                return false;
            }
        }
        return true;
    }
    
    for (let i = 2; i <= n; i++) {
        if (primeArray[i] && check_prime(i)) {
            answer += 1;
            for (let j = i * i; j <= n; j += i) {
                primeArray[j] = false;
            }
        }
    }
    
    return answer;
}