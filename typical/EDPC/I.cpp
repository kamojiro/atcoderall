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
  double p;
  int t = N/2 + 1;
  double dp[t+1] = {0};
  dp[0] = 1;
  for (int i = 0; i < N; ++i) {
    cin >> p;
    for (int j = t-1; j >= 0; --j) {
      dp[j+1] += dp[j]*p;
      dp[j] = dp[j]*(1-p);
    }
  }
  cout << dp[t] << "\n";
  return 0;
}
