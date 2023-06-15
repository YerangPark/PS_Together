import java.io.*;

public class BJ2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = 0;

        while (true) {

            int temp = br.read();

            if (temp < 'A')
                break;
            else if (temp < 'D')
                n += 3;
            else if (temp < 'G')
                n += 4;
            else if (temp < 'J')
                n += 5;
            else if (temp < 'M')
                n += 6;
            else if (temp < 'P')
                n += 7;
            else if (temp < 'T')
                n += 8;
            else if (temp < 'W')
                n += 9;
            else if(temp <= 'Z')
                n += 10;
        }
        System.out.print(n);
    }
    
}
