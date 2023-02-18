// 7의 개수
class Solution {
    public int solution(int[] array) {
        int answer = 0; // 7의 개수
        // array의 요소를 순회
        for (int i = 0; i < array.length; i++) {
            // 각 요소를 int -> string으로 형번환
            String element = Integer.toString(array[i]);
            // 각 요소를 그 요소의 길이만큼 반복
            for (int j = 0; j < element.length(); j++) {
                // 7이 있다면 +1
                if(element.charAt(j) == '7') {
                    answer++;
                }
            }
        }
        return answer;
    }
}
