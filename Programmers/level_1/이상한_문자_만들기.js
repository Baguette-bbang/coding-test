function solution(s) {
    var answer = '';
    s = s.split(" ");
    for (let i = 0; i < s.length; i++) {
        let word = s[i].split("");
        for (let j = 0; j < word.length; j++) {
            if (j%2 === 0) {
                answer += word[j].toUpperCase();
            } else {
                answer += word[j].toLowerCase();
            }
        }
        answer += ' ';
    }
    return answer.slice(0,-1);
}