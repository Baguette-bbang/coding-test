function solution(keymap, targets) {
    // 시작 시간 37분
    // 종료 시간 
    var answer = [];
    // keymap[i]는 i + 1번 키를 눌렀을 때 순서대로 바뀌는 문자
    // 알파벳 대문자로만 
    // 목표 문자열을 작성할 수 없을 때는 -1을 저장
    let keymaps = new Map();
    for (let i = 0; i < keymap.length; i++) {
        let keys = keymap[i].split('');
        for (let j = 0; j < keys.length; j++) {
            //keymaps[keys[j]] = keymaps[keys[j]] < j ? keymaps[keys[j]] : j;
            if (!keymaps.has(keys[j]) || keymaps.get(keys[j]) > j) {
                keymaps.set(keys[j], j);
            }
        }
    }
    console.log(keymaps)
    for (let target of targets) {
        let cnt = 0;
        let flag = true;
        for (let key of target.split('')) {
            if (keymaps.has(key)) {
                cnt += keymaps.get(key) + 1;
            } else {
                answer.push(-1);
                flag = false;
                break;
            }
        }
        if (flag) {
            answer.push(cnt);
        }   
    }
    return answer;
}