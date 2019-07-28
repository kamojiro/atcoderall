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
  string S;
  cin >> S;
  int N = S.size();
  ll dp[N+1][13];
  ll Q = 1000000009;
  ll r,t;
  char s;
  for (int i = 0; i < N+1; ++i) {
    for (int j = 0; j < 13; ++j) {
      dp[i][j] = 0;
    }
  }
  dp[0][0] = 0;
  for (int i = 0; i < N; ++i) {
    s = S[N-1-i];
    if (s == '?') {
      for (int k = 0; k < 10; ++k) {
        t = (k)
      }

    }
  }

  
  return 0;
}
