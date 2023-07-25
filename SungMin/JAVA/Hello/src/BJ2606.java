import java.io.*;
import java.util.*;

public class BJ2606 {
    static int[][] map;
    static int[] visited;
    static int n, m;
    static int count = 0;

    public static int dfs(int i) {
        visited[i] = 1;

        for (int k = 1; k <= n; k++) {
            if (map[i][k] == 1 && visited[k] == 0) {
                count++;
                dfs(k);
            }
        }
        return count;
    }

    // public static int bfs(int v) {
    //     Queue<Integer> q = new LinkedList<>();
    //     q.offer(v);
    //     visited[v] = 1;

    //     while (!q.isEmpty()) {
    //         int x = q.poll();

    //         for (int j = 1; j <= n; j++) {
    //             if (map[x][j] == 1 && visited[j] == 0) {
    //                 visited[j] = 1;
    //                 q.offer(j);
    //                 count++;
    //             }
    //         }
    //     }
    //     return count;
    // }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        map = new int[n+1][n+1];
        visited = new int[n+1];

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            map[a][b] = map[b][a] = 1;
        }
        System.out.println(dfs(1));
    }
}
