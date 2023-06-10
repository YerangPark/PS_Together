import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ1550 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine(), 16);
        System.out.println(A);
    }
}
