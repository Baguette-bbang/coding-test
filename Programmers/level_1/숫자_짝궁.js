function solution(X, Y) {
    var answer = '';
    // 1. 공통인 숫자 뽑기
        // 해당하는 숫자의 개수를 따지면 된다.
    // 2. 공통인 숫자 중 가장 큰 숫자 조합 찾기(가장 큰 숫자부터 정렬하기)
    // 3. 공통인 숫자가 없다면 -1 처리하기
    // 3,000,000 -> 시간제한 고려해야함.
    objX = new Map();
    objY = new Map();
    for (x of X) {
        objX.set(x, (objX.get(x) || 0) + 1);
    }
    for (y of Y) {
        objY.set(y, (objY.get(y) || 0) + 1); 
    }
    objX.forEach((value, key) => {
        if (objY.has(key)) {
            const minCnt = Math.min(value, objY.get(key));
            answer += key.repeat(minCnt);
        }
    })
    answer = answer.split('').sort((a, b) => b - a).join('');
    if (answer.startsWith('0')) {
        answer = '0';
    } else if (answer === '') {
        answer = '-1';
    }
    return answer;
}