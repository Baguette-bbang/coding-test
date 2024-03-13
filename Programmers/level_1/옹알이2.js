function solution(babbling) {
    var answer = 0;
    let canBabbling = ["aya", "ye", "woo", "ma"];
    // 위에 해당되는 조합?
    for (let i = 0; i < babbling.length; i++) {
        let prevBabbling = '';
        while (true) {
            let flag = true;
            for (let j = 0; j < canBabbling.length; j++) {
                if (babbling[i].startsWith(canBabbling[j]) && prevBabbling !== canBabbling[j]) {
                    babbling[i] = babbling[i].substring(canBabbling[j].length)
                    prevBabbling = canBabbling[j];
                    flag = false;
                    break;
                }
            }
            if (babbling[i] === '') {
                answer += 1;
                console.log(i)
                break; 
            } else if (flag) {
                break;
            }
        }
    }
    return answer;
}