function solution(arr, divisor) {
    let answer = [];
    arr.forEach(element => {
        if (element%divisor === 0) answer.push(element) 
    });
    return answer.length === 0 ? [-1] : answer.sort((a,b) => a-b);
}