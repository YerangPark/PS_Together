import java.io.*;

public class BJ11721 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        
        for (int i = 0; i < s.length(); i += 10) {
            if (i + 10 >= s.length()) {
                System.out.println(s.substring(i));
            } else {
                System.out.println(s.substring(i, i+10));
            }
        }
    }
}
