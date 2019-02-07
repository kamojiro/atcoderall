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
  int H, W;
  cin >> H >> W;
  string A[H];
  for (int i = 0; i < H; ++i) {
    cin >> A[i];
  }
  ll Q=1000000007;
  // ll dp[H][W];
  // for (int i = 0; i < H; ++i) {
  //   for (int j = 0; j < W; ++j) {
  //     dp[i][j] = 0;
  //   }
  // }
  vector<vector<ll>> dp(H, vector<ll>(W,0));
  dp[0][0] = 1;
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (i != H-1) {
        if (A[i+1][j] == '.') {
          dp[i+1][j] = (dp[i+1][j] + dp[i][j])%Q;
        }
      }
      if (j != W-1) {
        if (A[i][j+1] == '.') {
          dp[i][j+1] = (dp[i][j+1] + dp[i][j])%Q;
        }
      }
    }
  }
  cout << dp[H-1][W-1] << "\n";
  return 0;
}
