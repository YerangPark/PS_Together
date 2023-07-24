import java.io.*;

public class BJ2217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int min = 0;

        for(int i = 0; i < n; i++) {
            int k = Integer.parseInt(br.readLine());
            arr[i] = k;
        }
        min = arr[0];

        for (int i = 1; i < n; i++) {
            if (min > arr[i]) {
                min = arr[i];
            }
        }
        System.out.println(min*n);
    }
}
