import java.io.*;
import java.util.*;

public class BJ2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[8];

        for (int i = 0; i < 8; i ++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }
        int cnt = 0;
        for (int i = 0; i < 7; i++) {
            if (arr[i] + 1 == arr[i+1]) {
                cnt += 1;
            }
            else if (arr[i] - 1 == arr[i+1]) {
                cnt -= 1;
            }
        }
        if (cnt == 7) {
            System.out.println("ascending");
        }
        else if (cnt == -7) {
            System.out.println("descending");
        }
        else {
            System.out.println("mixed");
        }
    }
}