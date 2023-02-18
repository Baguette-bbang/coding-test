class Solution {
    public int solution(int n) {
        int answer = 2;
        double sqr = Math.sqrt(n);
        
        if (sqr == (int)sqr) answer = 1;
        
        return answer;
    }
}
