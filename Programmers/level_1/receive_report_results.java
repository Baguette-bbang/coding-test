import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // report 배열 중복제거(같은 신고는 1회로 처리하기 때문)
        LinkedHashSet<String> uniqueReport = new LinkedHashSet<>(Arrays.asList(report));
        // 다시 배열로 변환
        report = uniqueReport.toArray(new String[]{});
        // 신고자와 피신고자 배열생성
        ArrayList<String> reporter = new ArrayList<>(report.length), defendant = new ArrayList<>(report.length);
        int[] answer = new int[id_list.length];

        // report 배열의 요소를 꺼내 각각 신고자와 피신고자 배열로 나누어 넣어줌
        for (int i = 0; i < report.length; i++) {
            String[] reportTemp = report[i].split(" ");
            reporter.add(reportTemp[0]);
            defendant.add(reportTemp[1]);
        }
        // 각 유저의 신고당한 횟수 측정
        for (int i = 0; i < id_list.length; i++) {
            int reportNum = Collections.frequency(defendant, id_list[i]);
            // k번 이상 신고당한 유저
            if (reportNum >= k) {
                // k번 이상 신고당한 유저의 위치찾기
                for (int j = 0; j < defendant.size(); j++) {
                    // 피신고자 배열과 신고자 배열의 위치를 1대1 매칭함
                    if (id_list[i].equals(defendant.get(j))) {
                        // 제제당하는 유저를 신고한 유저의 위치에 +1
                        answer[Arrays.asList(id_list).indexOf(reporter.get(j))]++;
                    }
                }
            }
        }
        return answer;
    }
}
