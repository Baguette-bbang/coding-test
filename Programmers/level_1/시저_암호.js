function solution(s, n) {
    // 65~90 대문자
    // 97~122 소문자
    var answer = '';
    s = s.split('');
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") {
            answer += " ";
        } else {
            let ascii = s[i].charCodeAt() + n;
            if (s[i].charCodeAt() <= 90) { // 대문자
                ascii > 90 ? ascii = ascii % 90 + 64 : ascii;
            } else {
                console.log(ascii)
                ascii > 122 ? ascii = ascii % 122 + 96 : ascii;
            }
            answer += String.fromCharCode(ascii);
        }
    }
    return answer;
}