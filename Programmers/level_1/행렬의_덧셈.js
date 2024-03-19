function solution(arr1, arr2) {
    var answer = Array.from({length : arr1.length}, () => Array.from({length : arr1[0].length}, () => 0));
    // 같은 행 같은 열의 값을 서로 더한 결과
    for (let i = 0; i<arr1.length; i++) {
        for (let j = 0; j<arr1[i].length; j++) {
            answer[i][j] = arr1[i][j] + arr2[i][j]
        }
    }
    return answer;
}