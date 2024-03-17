function solution(numbers) {
    var answer = new Set();
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            answer.add(numbers[i] + numbers[j]);    
        }
    }
    answer = Array.from(answer).sort((a,b) => a-b);
    return answer;
}