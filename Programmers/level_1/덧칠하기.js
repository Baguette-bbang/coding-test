function solution(n, m, section) {
    var answer = 1;
    // 그리디하게 접근
    // 횟수 이기에 벽에서 넘어가는 것은 상관 없음.
    let start = section[0]
    section.shift()
    
    for (sect of section) {
        if (sect - start < m) {
            continue;
        } else {
            start = sect;
            answer += 1;
        }
    }
    return answer;
}