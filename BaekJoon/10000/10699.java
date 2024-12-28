import java.time.*;
import java.time.format.DateTimeFormatter;
public class Main {
public static void main(String args[]){
    ZonedDateTime koreaTime = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    String formattedTime = koreaTime.format(formatter);
    System.out.println(formattedTime);
  }
}
