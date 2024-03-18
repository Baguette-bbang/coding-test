function solution(N, stages) {
    var answer = [];
    // 동적으로 게임 시간을 늘려서 난이도를 조절
    // 실패율을 구하는 부분 구현
    // 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    // 도전했으나 실패한 사람의 수
    // n+1은 마지막까지 클리어한 사람임.
    // 각각 기능별로 쪼개기 
    // 1. 실패율 구하기
    // 전체에서 해당하는 스테이지의 숫자를 구하기
    
    let failure_num = new Array(N+2).fill(0);
    for (let i = 0; i < stages.length; i++) {
        failure_num[stages[i]] += 1
    } 
    
    let people_num = stages.length;
    let failure_rate = new Map;
    for(let i = 1; i < failure_num.length-1; i++) {
        failure_rate[i] = failure_num[i]/people_num;
        people_num -= failure_num[i];
    }
    
    // 객체를 [키, 값] 쌍의 배열로 변환
    let entries = Object.entries(failure_rate);

    // 배열 정렬
    entries
        .sort((a, b) => b[1] - a[1])
        .map(([key, value]) => 
            [parseInt(key), value])
        .forEach((a) => answer.push(a[0]));
    
    return answer;
}