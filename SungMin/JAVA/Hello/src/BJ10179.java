import java.io.*;

public class BJ10179 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            double x = Double.parseDouble(br.readLine());

            System.out.printf("$%.2f", x*0.8);
            System.out.println();
        }
    }
}
