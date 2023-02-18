import java.util.ArrayList;
// 문제 : 개인정보 수집 유효기간
class Solution {
    public ArrayList<Integer> solution(String today, String[] terms, String[] privacies) {
    	// 공백 또는 .으로 나누어져 오는 문자열을 저장하기 위함
        ArrayList<String> splitTerms = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        // 년도 월 일로 오는 날짜를 일수로만 바꿈
        int intToday = dateToDay(today);
		
        // 공백으로 나뉘어진 문자열 배열(terms)을 하나씩 꺼내어 저장
        for (int i = 0; i < terms.length; i++) {
            String[] temp= terms[i].split(" ");
            splitTerms.add(temp[0]);
            splitTerms.add(temp[1]);
        }
		
        // 각 사용자들의 계약 날짜와 약관종류를 토대로 만료된 계약을 찾아냄
        for (int i = 0; i < privacies.length; i++) {
        	// 공백을 기준으로 계약 날짜와 약관 종류로 나뉘어진 Privacies의 요소를 가져옴
            String[] tempPricacies = privacies[i].split(" ");
            // 사용자의 약관 종류를 토대로 위치를 찾고 +1을 하는 이유는 splitTerms는 (약관, 만료월수)로 이루어져있기때문이다.
            int index = splitTerms.indexOf(tempPricacies[1]) + 1;
            // 날짜를 일수로 변환한 후 계약기간(월수) 또한 일수로 바꾸어 더해줌
            // 즉 intPrivacies는 날짜 + 계약기간
            int intPrivacies = dateToDay(tempPricacies[0]) + Integer.parseInt(splitTerms.get(index)) * 28;
            // 계약한 날짜 + 계약기간이 오늘날짜보다 적거나 같으면 만료된 계약임
            if (intPrivacies <= intToday) {
                answer.add(i+1);
            }
        }

        return answer;
    }
    public static int dateToDay(String date) {
        int day = 0;

        String[] strDate = date.split("[.]");
        // 년도에서 월로 변환
        day += (Integer.parseInt(strDate[0]) - 2000) * 12;
        // 월에서 일수로 변환
        day = (day + Integer.parseInt(strDate[1])) * 28;
        // 일수 더하기
        day += Integer.parseInt(strDate[2]);

        return day;
    }
}