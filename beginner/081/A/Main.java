import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s = scan.next();
    char[] c = s.toCharArray();
    int ans = 0;
    for (char ch: c) {
      if (ch == '1') {
        ans++;
      }
    }
    System.out.println(ans);
  }
}

