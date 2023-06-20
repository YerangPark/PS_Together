import java.io.*;
import java.util.*;

public class BJ2309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        int sum = 0;
        int a = 0;
        int b = 0;
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];            
        }

        Arrays.sort(arr);

        for(int i = 0; i < arr.length; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if (sum - arr[i] - arr[j] == 100) {
                    a = arr[i];
                    b = arr[j];
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
            if (a == arr[i] || b == arr[i]) {
                continue;
            }
            System.out.println(arr[i]);
        }
    }
}
