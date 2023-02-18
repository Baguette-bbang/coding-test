import java.util.ArrayList;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        // 실제 조카가 말하는 옹알이들 종류
        String [] realBabbling = {"aya", "ye", "woo", "ma"};
        // 실제 조카가 말하는 옹알이들과 비슷한점이 얼만지 체크
        ArrayList<Integer> babblingCheck = new ArrayList<>();

        // 각 옹알이 길이로 babblingCheck 초기화
        for (int i = 0; i < babbling.length; i++) {
            babblingCheck.add(babbling[i].length());
        }

        // isInclud를 통해 조카가 발음할 수 있는 옹알이를 뺀 값을 저장
        for(int i = 0 ; i < babbling.length; i++) {
            for(int j = 0; j < realBabbling.length; j++){
                int num = isInclude(babbling[i], realBabbling[j]);
                babblingCheck.set(i, babblingCheck.get(i) - num);
            }
        }

        // 0(조카가 말할 수 있는 옹알이)이라면 answer의 개수 +1
        for(int i = 0; i < babblingCheck.size(); i++) {
            if(babblingCheck.get(i) == 0) {
                answer++;
            }
        }
        return answer;
    }
    // babbling과 realBabbling 사이의 일치하는 것을 찾고 해당 문자열의 개수를 반환
    public int isInclude(String babbling, String realBabbling){
        int numberOfString = 0;
        if (babbling.contains(realBabbling)) {
            numberOfString = realBabbling.length();
        }
        return numberOfString;
    }

}