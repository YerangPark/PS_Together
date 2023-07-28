import java.io.*;
import java.util.*;

public class BJ1260 {

    static int[][] map;
    static int[] visited;
    static int n, m, v;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        map = new int[n+1][n+1];
        visited = new int[n+1];

        for (int i = 0; i < m; i++) {
            StringTokenizer srt = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(srt.nextToken());
            int b = Integer.parseInt(srt.nextToken());

            map[a][b] = map[b][a] = 1;
        }

        dfs(v);

        System.out.println();
        visited = new int[n+1];

        bfs(v);

    }

    public static void dfs(int v) {
        visited[v] = 1;
        System.out.print(v + " ");

        for (int i = 1; i <= n; i++) {
            if (map[v][i] == 1 && visited[i] == 0) {
                dfs(i);
            }
        }
    }

    public static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        visited[v] = 1;
        q.offer(v);

        System.out.print(v + " ");

        while (!q.isEmpty()) {
            int x = q.poll();

            for (int i = 1; i <= n; i++) {
                if (map[x][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    q.offer(i);
                    System.out.print(i + " ");
                }
            }
        }
    }
}

