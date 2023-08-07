import java.io.*;
import java.util.*;

public class BJ2468 {
    static int[][] map;
    static int[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int n, cnt;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] > max) {
                    max = map[i][j];
                }
            }
        }

        for (int i = 0; i < max; i++) {
            cnt = 0;
            visited = new int[n][n];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (map[j][k] > i && visited[j][k] == 0) {
                        dfs(i, j, k);
                        cnt += 1;
                    }
                }
            }
            list.add(cnt);
        }
        int result = Collections.max(list);
        System.out.println(result);
    }
    public static void dfs(int v, int x, int y) {
        visited[x][y] = 1;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                if (map[nx][ny] > v && visited[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    dfs(v, nx, ny);
                }
            }
        }
    }
}