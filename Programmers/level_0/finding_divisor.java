import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int n) {
    	// 굳이 필요없지만 이해를 돕기위해 i*i 대신 써도 되는 변수
        double sqrt_n = Math.sqrt(n) + 1;
        ArrayList<Integer> answer = new ArrayList<>();
        // 반복문의 횟수를 줄이기 위해 i가 제곱근과 같거나 작을때까지만 반복
        for (int i = 1; i * i <= n; i++) {
        	// i가 제곱근일 경우 Ex) sqrt(100) = 10;
            if (i * i == n){
                answer.add(i);
            }
            // n이 i로 나누어 떨어졌을 경우
            else if(n % i == 0) {
                answer.add(i);
                answer.add(n / i);
            }
        }
        // 정렬
        Collections.sort(answer);
        return answer;
    }
}
