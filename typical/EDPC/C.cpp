#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()
int main()
{
  int N;
  cin >> N;
  int H[N][3];
  int dp[N][3];
  for (int i = 0; i < N; ++i) {
    cin >> H[i][0] >> H[i][1] >> H[i][2];
    }
  dp[0][0] = H[0][0];
  dp[0][1] = H[0][1];
  dp[0][2] = H[0][2];
  for (int i = 1; i < N; ++i) {
    int a = H[i][0];
    int b = H[i][1];
    int c = H[i][2];
    dp[i][0] = max( dp[i-1][1]+a, dp[i-1][2]+a);
    dp[i][1] = max( dp[i-1][0]+b, dp[i-1][2]+b);
    dp[i][2] = max( dp[i-1][0]+c, dp[i-1][1]+c);
  }
  cout << max({dp[N-1][0], dp[N-1][1], dp[N-1][2]}) << "\n";

  return 0;
}
