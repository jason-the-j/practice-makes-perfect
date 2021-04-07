import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    private static boolean[] visit = new boolean[1000001];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(solution(n));
    }

    private static int solution(int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);
        int count = 0;
        while (!queue.isEmpty()) {
            int len = queue.size();

            for (int i = 0; i < len; i++) {

                int num = queue.poll();
                if (num == 1) return count;
                if (num % 3 == 0 && !visit[num / 3]) {
                    visit[num / 3] = true;
                    queue.add(num / 3);
                }
                if (num % 2 == 0 && !visit[num / 2]) {
                    visit[num / 2] = true;
                    queue.add(num / 2);
                }
                if (!visit[num - 1]) {
                    visit[num - 1] = true;
                    queue.add(num - 1);
                }
            }
            count++;
        }
        return 0;
    }
}
