class Solution {
    public int solution(int[] common) {
        int answer = 0, diff = 0;
        // 등비수열인지, 등차수열인지 구분하기
        // 등차수열
        if (common[1]-common[0] == common[2]-common[1]) {
            diff = common[1] - common[0];
            answer = common[common.length - 1] + diff;
        }
        // 등비수열
        else{
            diff = common[1] / common[0];
            answer = common[common.length -1] * diff;
        }
        return answer;
    }
}
