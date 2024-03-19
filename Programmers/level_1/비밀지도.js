function solution(n, arr1, arr2) {
    var answer = [];
    // 각 칸은 공백 또는 벽으로 이루어져 있다.
    // 두 장의 지도를 겹쳐서 얻을 수 있다.
    // 둘 다 공백이면 공백, 둘 중 하나 벽 이면 벽
    // 벽은 1 공백은 0
    // 1. 1차원 숫자 배열 -> 2차원 바이너리 배열
    // 2. 벽인지 공백인지 탐색
    for (let i = 0; i < n; i++) {
        // 2진수로 변환
        let binary1 = arr1[i].toString(2)
        let binary2 = arr2[i].toString(2)

        // 앞자리 0 채우기
        if (binary1.length < n) {
            binary1 = '0'.repeat(n-binary1.length)+binary1
        }
        if (binary2.length < n) {
            binary2 = '0'.repeat(n-binary2.length)+binary2
        }
        
        // 스플릿하기
        binary1 = binary1.split('');
        binary2 = binary2.split('');

        // 벽인지 아닌지 체크
        let secret_map = ''
        for (let j = 0; j < n; j++) {
            if (binary1[j] === '1' || binary2[j] === '1') {
                secret_map += '#';
            } else {
                secret_map += ' ';
            }
        }
        answer.push(secret_map)
    }
    
    return answer;
}