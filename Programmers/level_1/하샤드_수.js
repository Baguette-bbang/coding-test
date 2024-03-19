function solution(x) {
    var answer = true;
    // 하샤드 수의 정의는?
    // x의 자릿수의 합으로 x가 나누어져야 한다.
    let digit = 0;
    x = String(x)
    for (let i = 0; i < x.length; i++) {
        digit += parseInt(x[i])
    }
    return parseInt(x)%digit==0 ? true : false;
}