import java.io.*;
import java.util.*;

public class BJ1931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int arr[][] = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, (a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        int cnt = 0;
        int num = 0;

        for (int i = 0; i < n; i++) {
            if (num <= arr[i][0]) {
                num = arr[i][1];
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
