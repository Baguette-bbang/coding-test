class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {};
        // 값 초기화
        int startX = -1, startY = -1, endX = -1, endY = -1;
        for (int i = 0; i < wallpaper.length; i++) {
            char[] row = wallpaper[i].toCharArray();
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (row[j] == '#') {
                    // 처음 나오는 '#'으로 초기화
                    if (startY == -1) {
                        startY = j;
                    }
                    // 가장 왼쪽의 '#'
                    if (startX == -1) {
                        startX = i;
                    }
                    // 가장 위쪽의 '#'
                    if (startY >= j) {
                        startY = j;
                    }
                    // 처음 나오는 '#'으로 초기화
                    if (endY == -1) {
                        endY = j + 1;
                    }
                    // 가장 오른쪽의 '#'
                    if (endY <= j) {
                        endY = j + 1;
                    }
                    // 가장 아래쪽의 '#'
                    endX = i + 1;
                }
            }
        }
        answer = new int []{startX, startY, endX, endY};
        return answer;
    }
}
