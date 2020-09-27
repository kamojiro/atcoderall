F

public class CountRangeCoveringRange {
    /**
     * Counts how many ranges in [l,r).
     * Answers multiple query.
     *
     * O((n+q)log(n+q) where q = query.length, n = ranges.length
     *
     * @param ranges array of [l,r)
     * @param query answerCountQuery query
     * @return answers to the queries
     */
    public static int[] answerCountQuery(int[][] ranges, int[][] query) {
        int n = ranges.length;
        int q = query.length;
        int[][] qinfo = new int[n+q][3];
        for (int i = 0; i < q ; i++) {
            qinfo[i] = new int[]{ query[i][0], query[i][1], i };
        }
        for (int i = 0; i < n ; i++) {
            qinfo[q+i] = new int[]{ ranges[i][0], ranges[i][1], -1 };
        }

        Arrays.sort(qinfo, (a, b) -> (a[1] == b[1]) ? a[2] - b[2] : a[1] - b[1]);

        // it may need value compression.
        FenwickTree bit = new FenwickTree(1000010);
        int[] ans = new int[q];
        int head = 0;
        for (int i = 0; i < n+q ; i++) {
            if (qinfo[i][2] == -1) {
                // target range
                bit.add(qinfo[i][0]+1, 1);
            } else {
                // query range
                ans[qinfo[i][2]] = (int)bit.range(qinfo[i][0]+1, qinfo[i][1]);
            }
        }
        return ans;
    }
}


public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // 入力を受け取る
    int N = sc.nextInt();
	int Q = sc.nextInt();
    int C[] = new int[N];
    int q[] = new q[Q][2];
    for (int i = 0; i < Q; i++) {
      int x = sc.nextInt();
      int y = sc.nextInt();
      q[i][0] = x;
      q[i][1] = y+1;
    }
    CountRangeCoveringRange CR = new CountRangeCoveringRange();
    int[] ans = CR.answerCountQuery(C,q);
    for (int i = 0; i < Q; i++) {
      System.out.println(ans[i]);      
    }

  }
}
