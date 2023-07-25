import java.util.*;
import java.io.*;

public class BJ2331 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        ArrayList<Integer> list = new ArrayList<>();

        list.add(a);

        while (true) {
            int tmp = list.get(list.size()-1); //다음 수 가져오기

            int result = 0; //자릿수 더한값
            while (tmp != 0) {
                result += (int) Math.pow(tmp % 10, p);
                tmp /= 10;
            }
            if (list.contains(result)) {
                int answer = list.indexOf(result);
                System.out.println(answer);
                break;
            }
            list.add(result);
        }
    }
}
