function solution(bandage, health, attacks) {
    var answer = 0;
    const last_attack = attacks[attacks.length-1][0];
    let continuous_cnt = 0;
    const limit_health = health;
    let attackIndex = 0;

    for (let i = 1; i <= last_attack; i++) {
        // 공격 시간인지 체크 
        if (i === attacks[attackIndex][0]) {
            // 공격 받음
            health -= attacks[attackIndex][1];
            continuous_cnt = 0;
            attackIndex++;
            if (health <= 0) {
                return -1;
            }
        } else { // 공격 시간이 아니라면 회복
            // t초만큼 연속 회복에 성공했다면
            continuous_cnt += 1;
            if (continuous_cnt === bandage[0]) {
                // y만큼 추가 회복
                health += bandage[2];
                health += bandage[1];
                continuous_cnt = 0;
            } else {
                health += bandage[1];
            }
            if (health > limit_health) {
                health = limit_health;
            }
        }
    }
    return health;
}