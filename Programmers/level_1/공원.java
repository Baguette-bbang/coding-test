import java.util.*;
class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        
        Arrays.sort(mats);
        for (int i = 0; i < mats.length/2; i++ ) {
            int temp = mats[i];
            mats[i] = mats[mats.length-1-i];
            mats[mats.length-1-i] = temp;
        }
        
        for (int i=0; i<mats.length; i++) {
            int matLength = mats[i];
            for (int j=0; j<=park.length - matLength; j++) {
                for (int z=0; z<=park[0].length - matLength; z++) {
                    if (park[j][z].equals("-1") && j+matLength <= park.length && z+matLength <= park[0].length) {
                        boolean check = false;
                        for(int r=0; r < matLength; r++) {
                            for (int c=0; c < matLength; c++) {
                                if (!park[r+j][c+z].equals("-1")) {
                                    check = true;
                                    System.out.println(r+ " " + c);
                                    break;
                                }
                            }
                            if (check) {
                                break;
                            }
                        }
                        if (!check) {
                            return matLength;
                        }
                    }
                }
            }
        }
        return -1;
    }
}