import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        // 햄버거의 개수
        int answer = 0;
        // remove를 사용하기 위해 ArrayList 사용
        ArrayList<Integer> hambuger = new ArrayList<>();
        // 재료 요소들을 하나씩 꺼내가며 레시피와 맞는지 비교
        for (int i = 0; i < ingredient.length; i++) {
            hambuger.add(ingredient[i]);
            // 햄버거의 조건 레시피(1,2,3,1)이 맞는지 재료가 4개 이상인지 확인
            if ((hambuger.size() >= 4) &&
                    (hambuger.get(hambuger.size()-1) == 1) &&
                    (hambuger.get(hambuger.size()-2) == 3) &&
                    (hambuger.get(hambuger.size()-3) == 2) &&
                    (hambuger.get(hambuger.size()-4) == 1)
            ) {
            	// 맞다면 만들어진 햄버거 개수 추가
                answer++;
                // 만든 재료들은 삭제
                for (int j = 0; j < 4; j++) {
                    hambuger.remove(hambuger.size()-1);
                }
            }
        }
        return answer;
    }
}