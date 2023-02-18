class Solution {
    public int solution(String A, String B) {
        int answer = 0;
        for (int i = 0; i < A.length(); i++) {
            if (A.equals(B)) {
                break;
            }
            else{
                answer ++;
                A = A.substring(A.length()-1)+ A.substring(0, A.length()-1); // 반복문을 돌 때마다 문자열을 오른쪽으로 한칸씩 밀기
            }
        }
        if(answer == A.length()) { answer = -1; } // 한바퀴를 돌았는데도 같지 않다면 다른 문자열이므로 -1
        return answer;
    }
}
