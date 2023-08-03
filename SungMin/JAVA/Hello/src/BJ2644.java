import java.io.*;
import java.util.*;

public class BJ2644 {
    static int[][] map;
    static int[] visited;
    static int n, a, b, m;
    static int[] count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());
        map = new int[n+1][n+1];
        visited = new int[n+1];
        count = new int[n+1];

        for (int i = 0; i < m; i++) {
            StringTokenizer srt = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(srt.nextToken());
            int y = Integer.parseInt(srt.nextToken());

            map[x][y] = map[y][x] = 1;
        }
        //dfs(a);
        bfs(a);

        if (count[b] > 0) {
            System.out.println(count[b]);
        } else {
            System.out.println(-1);
        }
    }

    public static void dfs(int a) {
        visited[a] = 1;

        for (int i = 1; i <= n; i++) {
            if (map[a][i] == 1 && visited[i] == 0) {
                count[i] = count[a] + 1;
                dfs(i);
            }
        }
    }

    public static void bfs(int a) {
        Queue<Integer> q = new LinkedList<>();
        visited[a] = 1;
        q.offer(a);

        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 1; i <= n; i++) {
                if (map[x][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    q.offer(i);
                    count[i] = count[x] + 1;
                }
            }
        }
        
    }
}
