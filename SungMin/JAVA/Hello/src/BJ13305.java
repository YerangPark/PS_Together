import java.io.*;
import java.util.*;

public class BJ13305 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int[] dist = new int[n-1];
        int[] cost = new int[n];

        for (int i = 0; i < n-1; i++) {
            dist[i] = Integer.parseInt(st.nextToken());
            cost[i] = Integer.parseInt(stk.nextToken());
        }
        long min_cost = cost[0];
        long result = 0;

        for (int i = 0; i < n-1; i++) {
            if (min_cost > cost[i]) {
                min_cost = cost[i];
            }
            result += min_cost * dist[i];
        }
        System.out.println(result);
    }
}
