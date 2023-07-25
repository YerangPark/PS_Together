import java.io.*;
import java.util.*;

public class BJ10451 {
    static int[] map;
    static int[] visited;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            map = new int[n+1];
            visited = new int[n+1];
            int count = 0;

            for (int j = 1; j <= n; j++) {
                map[j] = Integer.parseInt(st.nextToken());
            }

            for (int k = 1; k <= n; k++) {
                if (visited[k] == 0) {
                    count++;
                    bfs(k);
                }
            }
            System.out.println(count);
        }
    }
    public static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);
        visited[v] = 1;

        while (!q.isEmpty()) {
            int x = q.poll();
            int a = map[x];
            if (visited[a] == 0) {
                visited[a] = 1;
                q.offer(a);
            }
        }
    }
}

