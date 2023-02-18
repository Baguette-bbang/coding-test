// 잘라서 배열로 저장하기
class Solution {
    public String[] solution(String my_str, int n) {
        double temp = (double)my_str.length()/n;
        int size = (int) Math.ceil(temp);
        String[] answer = new String[size];

        // 반복횟수 : 문자열 길이 / 자르는 길이
        // 접근 오류를 막기 위해 배열의 마지막 자리에는 반복문을 나와 나머지 문자열 넣기
        for (int i = 0; i < size-1; i++) {
            // my_str을 n만큼 잘라서 answer에 넣고 나머지는 다시 대입
            answer[i] = my_str.substring(0,n);
            my_str = my_str.substring(n);
        }
        answer[size-1] = my_str;

        return answer;
    }
}
