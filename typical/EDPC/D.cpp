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
  int N, W;
  cin >> N >> W;
  int WV[N][2];
  for (int i = 0; i < N; ++i) {
    cin >> WV[i][0] >> WV[i][1];
  }
  ll dp[W+1] = {0};
  for (int i = 0; i < N; ++i) {
    int w = WV[i][0];
    int v = WV[i][1];
    for (int j = W; w <= j; --j) {
      dp[j] = max( dp[j], dp[j-w]+v);
    }
  }
  cout << dp[W] << "\n";
  return 0;
}
