package Programmers.level_2;

public class Solution {
  private static int[] v1;  // 열 체크
  private static int[] v2;  // / 방향 대각선 체크
  private static int[] v3;  // \ 방향 대각선 체크
  private static int answer;  // 가능한 경우의 수

  public static void dfs(int n, int size) {
      if (size == n) {
          answer += 1;
          return;
      }
      
      for (int j = 0; j < n; j++) {
          if (v1[j] == 0 && v2[size + j] == 0 && v3[size - j + n - 1] == 0) {
              // 퀸 배치
              v1[j] = v2[size + j] = v3[size - j + n - 1] = 1;
              dfs(n, size + 1);
              
              // 퀸 제거 (백트래킹)
              v1[j] = v2[size + j] = v3[size - j + n - 1] = 0;
          }
      }
  }

  public static int solution(int n) {
      v1 = new int[n];         // 열 체크
      v2 = new int[2 * n];     // / 방향 대각선
      v3 = new int[2 * n];     // \ 방향 대각선
      answer = 0;              // 결과 초기화

      dfs(n, 0);               // 0행부터 시작
      return answer;
  }
} {
  
}
