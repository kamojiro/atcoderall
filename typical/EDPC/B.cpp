#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
#include <cstdlib>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()
int main()
{
  int N, K, h, now;
  cin >> N >> K;
  int H[N], dp[N];
  for (int i = 0; i < N; ++i) {
    cin >> H[i];
  }
  dp[0] = 0;
  for (int i = 1; i < N; ++i) {
    h = H[i];
    now = dp[i-1] + abs( h - H[i-1] );
    for (int j = max(i-K,0); j < i; ++j) {
      if (now > dp[j] + abs( h - H[j])){
        now = dp[j] + abs( h - H[j]);
      }
    }
    dp[i] = now;
  }
  cout << dp[N-1] << "\n";
  return 0;
}
