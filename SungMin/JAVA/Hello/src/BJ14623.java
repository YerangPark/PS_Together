import java.io.*;

public class BJ14623 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long a = Long.parseLong(br.readLine(), 2);
        long b = Long.parseLong(br.readLine(), 2);

        String num = Long.toBinaryString(a*b);

        System.out.println(num);
    }
}
