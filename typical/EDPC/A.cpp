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
  int N;
  cin >> N;
  int dp[N];
  int H[N];
  for (int i = 0; i < N; ++i) {
    cin >> H[i];
  }
  dp[1] = abs(H[1]-H[0]);
  for (int i = 2; i < N; ++i) {
    dp[i] = min( dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]));
  }
  cout << dp[N-1] << "\n";
  return 0;
}
