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
  string s, t;
  cin >> s >> t;
  int ls = s.length(), lt = t.length();
  int dp[lt+1][ls+1] = {0};
  for (int i = 0; i < lt+1; ++i) {
    dp[i][0] = 0;
  }
  for (int i = 0; i < ls+1; ++i) {
    dp[0][i] = 0;
  }


  for (int i = 1; i < lt+1; ++i) {
    for (int j = 1; j < ls+1; ++j) {
      if(t[i-1] == s[j-1]){
        dp[i][j] = dp[i-1][j-1] + 1;
      }else {
        dp[i][j] = max( dp[i-1][j], dp[i][j-1]);
      }
    }
  }
  int i = lt, j = ls;
  string ans = "";
  while (i > 0 && j > 0) {
    if (t[i-1] == s[j-1]) {
      ans = t[i-1] + ans;
      i--; j--;
    }else {
      if (dp[i-1][j] >= dp[i][j-1]) {
        i--;
      }else {
        j--;
      }
    }
    // cout << i << j << ans << "\n";
  }
  cout << ans << "\n";

  return 0;
}
