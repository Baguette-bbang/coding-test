function solution(s) {
    var answer = 0;
    let startC = '';
    let isC = 0;
    let notIsC = 0;
    let temp = ''
    for (c of s.split('')) {
        if (temp == '') {
            startC = c;
        }
        temp += c
        if (c == startC) {
            isC += 1;
        } else {
            notIsC += 1;
        } 
        
        if (isC == notIsC) {
            answer += 1;
            temp = '';
            isC = 0;
            notIsC = 0;
        }
    } 
    if (temp != '') {
        answer += 1;
    }
    return answer;
}