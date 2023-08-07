import java.io.*;
import java.util.*;

public class BJ2667 {
    static int[][] map;
    static int n, cnt;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        ArrayList<Integer> list = new ArrayList<>();
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = s.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) {
                    map[i][j] = 0;
                    cnt = 1;
                    //dfs(i, j);
                    bfs(i, j);
                    list.add(cnt);
                }
            }
        }
        System.out.println(list.size());
        for (int i : list) {
            System.out.println(i);
        }
    }

    public static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {x, y});

        while (!q.isEmpty()) {
            int[] p = q.poll();
            int a = p[0];
            int b = p[1];

            for (int i = 0; i < 4; i++) {
                int nx = a + dx[i];
                int ny = b + dy[i];

                if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                    if (map[nx][ny] == 1) {
                        map[nx][ny] = 0;
                        cnt += 1;
                        q.offer(new int[] {nx, ny});
                }
            }
        } 
    }
}

    public static void dfs(int x, int y) {

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                if (map[nx][ny] == 1) {
                    map[nx][ny] = 0;
                    cnt += 1;
                    dfs(nx, ny);
                }
            }
        }
    }
}