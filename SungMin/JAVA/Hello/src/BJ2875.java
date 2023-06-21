import java.io.*;
import java.util.*;

public class BJ2875 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int team = 0;

        while (n >= 2 && m >= 1 && n + m - 3 >= k) {
            n -= 2;
            m --;   
            team ++;
        }
        System.out.println(team);
    }
}
