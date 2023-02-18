import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int n, int[] numlist) {
    	// add 메소드를 사용하기 위해 ArrayList사용
        ArrayList<Integer> answer = new ArrayList<Integer>();
        // 특정 수의 배수라는 것은 나눴을 때 나머지가 0이라는 뜻
        for (int i = 0; i < numlist.length; i++) {
            if (numlist[i] % n == 0){
                answer.add(numlist[i]);
            }
        }
        return answer;
    }
}
