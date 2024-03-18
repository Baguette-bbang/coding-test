function solution(dartResult) {
    var answer = 0;
    // 다트 게임은 총 3번의 기회
    // 기회마다 얻는 점수는 0~10점
    // S, D, T 영역이 존재
    // * : 전전점수와 전점수를 2배로
    // # : 해당 점수는 마이너스
    // 1. 숫자는 담고 -> s, d, t
    // 2. 배열에 담아둔다.
    // 3. 스타나 아치라면? 
    
    let score = new Array();
    let number = '';
    for (let i = 0; i < dartResult.length; i++) {
        // 숫자라면
        if (!isNaN(+dartResult[i])) {
            number += dartResult[i];
        } else { // 숫자가 아니라면
            if (number != ''){
                score.push(parseInt(number));
                number = '';
            }
            // D,T 처리
            if (dartResult[i] !== '*' && dartResult[i] !== '#'){
                if (dartResult[i] === 'D') {
                    score[score.length-1] = score[score.length-1]**2
                } else if (dartResult[i] === 'T') {
                    score[score.length-1] = score[score.length-1]**3
                }          
            } else { // *, # 처리
                if (dartResult[i] === '*') {
                    score[score.length-1] *= 2;
                    if (score[score.length-2] !== undefined) {
                        score[score.length-2] *= 2;
                    }
                } else {
                    score[score.length-1] *= -1;
                }
            }
        }
        console.log(score)
    }
    score.forEach((a) => answer += a)
    return answer;
}