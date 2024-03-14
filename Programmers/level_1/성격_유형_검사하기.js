function solution(survey, choices) {
    // 시작 시간 10분
    // 종료 시간 53분
    var answer = ['R', 'C', 'J', 'A']; // 디폴트값
    let types = new Map();
    // 매우 비동의부터 매우 동의까지 점수대가 총 7개
    // 해당 성격에 대한 검사가 없다면 사전순으로 배치 즉, 디폴트 값이 있다는 것.
    // 1~3점이면 4점에서 빼고, 5~7점이면 4점을 뺀다.
    
    for (let i = 0; i < survey.length; i++) {
        if (choices[i] < 4) {
            types.set(survey[i][0], (types.get(survey[i][0]) || 0) + (4 - choices[i]));
        } else if (choices[i] > 4) {
            types.set(survey[i][1], (types.get(survey[i][1]) || 0) + (choices[i] - 4));
        }
    }
    
    const typePairs = ['RT', 'CF', 'JM', 'AN'];
    for (let i = 0; i < typePairs.length; i++) {
        if ((types.get(typePairs[i][0]) || 0) >= (types.get(typePairs[i][1]) || 0)) {
            answer[i] = typePairs[i][0];
        } else {
            answer[i] = typePairs[i][1];
        }
    }
    return answer.join('');
}