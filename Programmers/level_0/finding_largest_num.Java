import java.util.Arrays;

class Solution {
    public int[] solution(int[] array) {
    	// 가장 큰 수와 그 위치를 저장하는 배열
        int[] answer = new int[2];
        // 입력으로 받은 숫자 배열을 문자열 배열로 변환(.indexOf()를 쓰기위해)
        String[] str_array = new String[array.length];
        for (int i = 0; i < array.length; i++) {
            str_array[i] = String.valueOf(array[i]);
        }
        // 배열에서 가장 큰 수를 찾고 정수로 형변환
        answer[0] = Arrays.stream(array).max().getAsInt();
        // 가장 큰 수를 찾은 결과값을 다시 문자열로 형변환한 후 indexOf로 해당 위치를 찾고 그 위치를 넣기
        answer[1] = Arrays.asList(str_array).indexOf(String.valueOf(answer[0]));
        
        return answer;
    }
}
