import java.util.*;
// 문제 : 둘만의 암호
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        ArrayList<String> alphabetList = new ArrayList<>();
        char[] skipArr = skip.toCharArray();
        char[] sArr = s.toCharArray();
        char alphabet = 'a';

        // 알파벳리스트 생성;
        for (int i = 0; i < 26; i++) {
            alphabetList.add(String.valueOf(alphabet));
            alphabet++;
        }
        // 알파벳리스트에서 skip에 있는 알파벳 삭제
        for (int i = 0; i < skipArr.length; i++) {
            int skipIndex = alphabetList.indexOf(Character.toString(skipArr[i]));
            alphabetList.remove(skipIndex);
        }
        // 알파벳리스트에서 sArr의 요소 위치를 찾아 +index 해주기
        for (int i = 0; i < sArr.length; i++) {
            int sIndex = alphabetList.indexOf(Character.toString(sArr[i]));
            while((sIndex + index) >= alphabetList.size()) {
                sIndex -= alphabetList.size();
            }
            answer += alphabetList.get(sIndex + index);
        }
        return answer;
    }
}