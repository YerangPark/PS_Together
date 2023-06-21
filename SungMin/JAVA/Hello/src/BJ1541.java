import java.io.*;

public class BJ1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split("-");
        int sum = 0;
        
        for (int i = 0; i < s.length; i++) {
            int res = 0;
            String[] div = s[i].split("\\+");
            
            for (int j = 0; j < div.length; j++) {
                
                res += Integer.parseInt(div[j]);
            }
            if (i == 0) {
                sum += res;
            } else {
                sum -= res;
            }
        }
        System.out.println(sum);
    }
}