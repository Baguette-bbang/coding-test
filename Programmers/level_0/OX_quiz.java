class Solution {
    public String[] solution(String[] quiz) {
        // temp는 quiz의 요소 하나의 수식과 결과값을 쪼개서 저장하는 곳
        String[] temp = {}, answer = new String[quiz.length];
        // quiz의 수만큼 반복
        for (int i = 0; i < quiz.length; i++) {
        	// quiz의 요소는 공백으로 숫자와 연산자가 나누어져 있기에 .split으로 쪼갠 후 저장
            temp = quiz[i].split(" ");
            // 퀴즈의 실제 연산값을 저장하는 곳
            int result = 0;
            // 연산자는 '-' 또는 '+'이기에 '+'인지 판별
            if (temp[1].equals("+")) {
                result = Integer.parseInt(temp[0]) + Integer.parseInt(temp[2]);
            }
            // '+'가 아니라면 '-'
            else {
                result = Integer.parseInt(temp[0]) - Integer.parseInt(temp[2]);
            }
            // 퀴즈의 연산값과 퀴즈의 요소에 적혀있는 값과 같은지 삼항연산자로 비교 후 answer에 'O', 'X' 대입
            answer[i] = (result == Integer.parseInt(temp[4])) ? "O" : "X";
        }
        return answer;
    }
}
