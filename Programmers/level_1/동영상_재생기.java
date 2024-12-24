import java.util.*;
class Solution {
    public int timeProcess(String command, int second) {
        if (command.equals("next")) {
            return second + 10;
        } else {
            return second - 10;
        }
    }
    public int startEndVal(int curTime, int videoLen) {
        if (curTime > videoLen) {
            return videoLen;
        } else if (curTime < 0) {
            return 0;
        } else {
            return curTime;
        }
    }
    
    public int opVal(int curTime, int opStart, int opEnd) {
        if (opStart<= curTime && curTime <= opEnd) {
            return opEnd;
        } else {
            return curTime;
        }
    }
    
    public int convertToSecond(String stringTime) {
        String[] stringTimes = stringTime.split(":");
        return Integer.parseInt(stringTimes[0])*60 + Integer.parseInt(stringTimes[1]);
    }
    
    public String convertToStringTime(int secondTime) {
        if (secondTime == 0) {
            return "00:00";
        } else {
            int minutes = secondTime/60;
            int seconds = secondTime%60;
            String result;
            if (minutes < 10) {
                result = "0" + String.valueOf(minutes);
            } else {
                result = String.valueOf(minutes);
            }
            result += ":";
            if (seconds < 10) {
                result += "0" + String.valueOf(seconds);
            } else {
                result += String.valueOf(seconds);
            }
            
            return result;
        }
    }
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        int intVideoLen = convertToSecond(video_len);
        int intPos = convertToSecond(pos);
        int intOpStart = convertToSecond(op_start);
        int intOpEnd = convertToSecond(op_end);
        
        for (String command : commands) {
            intPos = opVal(intPos, intOpStart, intOpEnd);
            intPos = timeProcess(command, intPos);
            intPos = opVal(intPos, intOpStart, intOpEnd);
            intPos = startEndVal(intPos, intVideoLen);   
        }
        answer = convertToStringTime(intPos);
        return answer;
    }
}