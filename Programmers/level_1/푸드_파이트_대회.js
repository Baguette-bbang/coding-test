function solution(food) {
    var answer = '';
    // 1. 1부터 홀수라면 -1하고 반으로 나누기 짝수라면 반으로 나누기
    // 2. 문자열 만들고 +  0 붙이기 + 뒤집기
    
    for (let i = 1; i < food.length; i++) {
        if (food[i]%2 !== 0) {
            food[i] -= 1;
        }
        answer += String(i).repeat(food[i]/2)
    }
    let reverseStr = answer.split('').reverse().join('');
    
    return answer + '0' + reverseStr;
}