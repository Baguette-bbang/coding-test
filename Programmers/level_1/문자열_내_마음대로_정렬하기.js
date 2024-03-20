function solution(strings, n) {
    var answer = [];
    // 각 요소의 n번째 문자를 기준으로 해서 오름차순 정렬
    // n번째 앞의 요소를 슬라이싱해서 딕셔너리형태로 만들고 나중에 합치기
    strings.sort(function (a,b) {
        if (a[n] > b[n]) {
            return 1;
        } else if (a[n] === b[n]) {
            if (a > b) {
                return 1;
            } else if (a < b) {
                return -1;
            } else {
                return 0;
            }
        } else {
            return -1;
        }
    });
    return strings;
}