import java.io.*;
import java.util.*;

public class BJ11724 {
    static int[][] map;
    static int[] visited;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n+1][n+1];
        visited = new int[n+1];

        for (int i = 0; i < m; i++) {
            StringTokenizer srt = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(srt.nextToken());
            int b = Integer.parseInt(srt.nextToken());

            map[a][b] = map[b][a] = 1;
        }

        int count = 0;

        for (int i = 1; i <= n; i++) {
            if (visited[i] == 0) {
                bfs(i);
                count += 1;
            }
        }
        System.out.println(count);
    }

    public static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);
        visited[v] = 1;

        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 1; i <= n; i++) {
                if (map[x][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    q.offer(i);
                }
            }
        }
    }

    public static void dfs(int v) {
        visited[v] = 1;

        for (int i = 1; i <= n; i++) {
            if (map[v][i] == 1 && visited[i] == 0) {
                dfs(i);
            }
        }
    }
}
