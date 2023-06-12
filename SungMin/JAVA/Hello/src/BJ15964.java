import java.io.*;
import java.util.*;

public class BJ15964 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long n = a+b;
        long m = a-b;
        
        System.out.println(n*m);
    }
}
