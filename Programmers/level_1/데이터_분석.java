
import java.util.*;

class Solution {
    public int getColNum(String colName) {
        if (colName.equals("code")) return 0;
        else if (colName.equals("date")) return 1;
        else if (colName.equals("maximum")) return 2;
        else return 3;
    }
    
    public int[][] filterRows(int[][] data, int intExt, int valExt) {
        List<int[]> filteredRows = new ArrayList<>();
        for (int[] row : data) {
            if (row[intExt] < valExt) {
                filteredRows.add(row);
            }
        }
        for (int[] row : filteredRows) {
            System.out.println(Arrays.toString(row));
        }
        return filteredRows.toArray(new int[0][]);
    }
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        
        int intExt = getColNum(ext);
        int intSortBy = getColNum(sort_by);
        
        int[][] filteredRows = filterRows(data, intExt, val_ext);
        Arrays.sort(filteredRows, Comparator.comparingInt(o -> o[intSortBy])); 
        return filteredRows;      
    }
}