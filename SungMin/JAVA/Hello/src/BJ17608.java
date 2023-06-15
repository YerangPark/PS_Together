import java.io.*;

public class BJ17608 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] x = new int[n];

        for(int i = 0; i < n; i++) {
            x[i] = Integer.parseInt(br.readLine());
        }

        int count = 0;
        int temp = 0;
        for (int i = n-1; i >= 0; i--) {
            if (temp < x[i] && temp != x[i]) {
                temp = x[i];
                count ++;
            }
        }
        System.out.println(count);
    }
}
