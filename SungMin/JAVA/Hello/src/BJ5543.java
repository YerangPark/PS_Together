import java.io.*;

public class BJ5543 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int h = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int l = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        int s = Integer.parseInt(br.readLine());

        System.out.println(Math.min(Math.min(h, m), l) + Math.min(c, s) - 50);
    }
}
