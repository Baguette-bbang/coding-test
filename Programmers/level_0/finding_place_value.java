class Solution {
    public int solution(int n) {
        int answer = 0;
        // n의 자릿수 길이를 저장 : 문자열로 변환하여 길이를 구함.
        int n_size = String.valueOf(n).length();
        // n의 자릿수 길이만큼 반복
        for(int i =0; i < n_size; i ++) {
            // answer에 자릿수를 하나씩 더함
            answer += n % 10;
            // answer에 더한 자릿수를 제외한 나머지 값들을 n에 저장
            n /= 10;
        }

        return answer;
    }
}
