import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.StringTokenizer;
public class BJ10757 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine());
        BigInteger A = new BigInteger(s.nextToken());
        BigInteger B = new BigInteger(s.nextToken());

        System.out.println(A.add(B));
    }
}
