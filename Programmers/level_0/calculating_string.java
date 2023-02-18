class Solution {
    public int solution(String my_string) {
        int answer = 0;
        // 공백을 기준으로 문자열을 쪼개 배열로 만듬
        String[] str_arr = my_string.split(" ");
      
        // 숫자 수식 숫자의 단계를 거친 후 수식 숫자 패턴이 나오기에 이를 먼저 처리함
        // 3 + 2 - 1 이라고 하면 3 + 2를 먼저 처리하고 - 1을 반복문으로 돌림
        if (str_arr[1].equals("+")) {
            answer = Integer.parseInt(str_arr[0]) + Integer.parseInt(str_arr[2]);
        } else {
            answer = Integer.parseInt(str_arr[0]) - Integer.parseInt(str_arr[2]);
        }
        
        for (int i = 3; i < str_arr.length; i++) {
            if (str_arr[i].equals("+")) {
                answer += Integer.parseInt(str_arr[i + 1]);
            } else {
                answer -= Integer.parseInt(str_arr[i + 1]);
            }
            // 위에서 이미 수식을 통해 숫자를 계산했기에 숫자는 건너 뜀
            i++;
        }
        System.out.println(answer);
        return answer;
    }
}
