// 문자열 정렬하기 (2)
import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        my_string = my_string.toLowerCase(); // 문자열을 소문자로 변환
        char[] my_ascii = new char[my_string.length()]; // 문자열을 문자로 쪼개 넣을 공간

        // 문자열을 문자로 쪼갬
        for (int i = 0; i < my_string.length(); i++) {
            my_ascii[i] = my_string.charAt(i);
        }

        // 아스키코드순(알파벳순)으로 정렬
        Arrays.sort(my_ascii);

        // 각 알파벳 순서대로 정렬된 문자들을 문자열로 변환
        for (int i = 0; i < my_ascii.length; i++) {
            answer += my_ascii[i];
        }
        return answer;
    }
}
