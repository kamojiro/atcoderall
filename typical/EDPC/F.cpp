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
  int LCS[lt+1][ls+1] = {0};
  string LC[lt+1][ls+1] = {""};
  for (int i = 1; i < lt+1; ++i) {
    for (int j = 1; j < ls+1; ++j) {
      if(t[i-1] == s[j-1]){
        LCS[i][j] = LCS[i-1][j-1] + 1;
        LC[i][j] = LC[i-1][j-1] + t[i-1];
      }else {
        if (LCS[i][j-1] <= LCS[i-1][j]) {
          LCS[i][j] = LCS[i-1][j];
          LC[i][j] = LC[i-1][j];
        }else {
          LCS[i][j] = LCS[i][j-1];
          LC[i][j] = LC[i][j-1];
        }
      }
    }    
  }
  cout << LC[lt][ls] << "\n";
  return 0;
}
