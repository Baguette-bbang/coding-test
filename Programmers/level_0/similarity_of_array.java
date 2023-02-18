class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        // s1의 요소 하나와 s2를 비교하여 같은 것은 찾아냄
        for (int i = 0; i < s1.length; i++) {
            for (int j = 0; j < s2.length; j++) {
                if (s1[i].equals(s2[j])) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}
