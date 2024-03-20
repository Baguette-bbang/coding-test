function solution(arr) {
    var answer = 0;
    let sum = 0;
    arr.forEach((a)=>answer+=a)
    return answer/arr.length;
}