import java.io.*;

public class BJ17362 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine()) % 8;
     
        if (n == 0) {
            System.out.println(2);
        } else if (n == 6) {
            System.out.println(4);
        } else if (n == 7) {
            System.out.println(3);
        } else {
            System.out.println(n);
        }
    }
}
