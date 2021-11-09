import java.io.*;
import java.util.*;

class Main{
        static final int MAX = Integer.MAX_VALUE;
  public static void main(String args[]) throws Exception {
       int T;
        int K;
        int[] C;
        int[] S;
        int[][] dp;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++)
        {

            K = Integer.parseInt(br.readLine());
            C = new int[K + 1];
            S = new int[K + 1];
            dp = new int[K + 1][K + 1];

            S[0] = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i < K + 1; i++)
            {
                C[i] = Integer.parseInt(st.nextToken());
                S[i] = S[i - 1] + C[i];
                for (int j = 1; j < K + 1; j++)
                {
                    dp[i][j] = -1;
                }
            }
            System.out.println(solve(dp, C, S,1, K));
        }
    }

    static int solve(int[][] dp, int[] C, int[] S, int start, int end)
    {
        if (start >= end)
        {
            return 0;
        }
        if (end == start + 1)
        {
            return C[start] + C[end];
        }
        if(dp[start][end]==-1){
            dp[start][end] = MAX;
            for (int i = start; i < end; i++)
            {
                int temp = solve(dp, C, S, start, i) + solve(dp, C, S, i + 1, end) + S[end] - S[start - 1];
                dp[start][end] = Math.min(dp[start][end], temp);
            }
        }
        return dp[start][end];
    }
}
