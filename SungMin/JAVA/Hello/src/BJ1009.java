import java.io.*;
import java.util.*;

public class BJ1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int x1 = Integer.parseInt(st.nextToken());
        int y1 = Integer.parseInt(st.nextToken());
        int x2 = Integer.parseInt(st.nextToken());
        int y2 = Integer.parseInt(st.nextToken());

        int[] arr = new int[4];
        arr[0] = x2-x1;
        arr[1] = y2-y1;
        arr[2] = x1;
        arr[3] = y1;

        System.out.println(Arrays.stream(arr).min().getAsInt());
    }
}
