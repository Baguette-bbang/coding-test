class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        // 등차수열의 합 공식 이용 Sn = n(a + l)/2
        // Sn = total, n = num, l = a + num - 1
        int startNum = (total * 2 / num - num + 1) / 2;
        
        // answer에 a(시작수) 부터 l(끝 수) 까지 대입
        for(int i = 0; i < num; i++) {
            answer[i] = startNum;
            startNum ++;
        }
        return answer;
    }
}
