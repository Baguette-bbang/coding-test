import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] dice = new int[3];
        int count = 0, result = 0; // 같은 수를 세는 용도
        // 입력
        for (int i = 0; i < 3; i++) {
            dice[i] = sc.nextInt();
        }
        // 정렬
        Arrays.sort(dice);

        if (dice[0] == dice[1]){
            if (dice[1] == dice[2]) {
                result = 10000 + dice[0] * 1000;
            }
            else{
                result = 1000 + dice[0] * 100;
            }
        }
        else if (dice[1] == dice[2]){
            result = 1000 + dice[1] * 100;
        }
        else{
            result = dice[2] * 100;
        }

        System.out.println(result);
    }
}
