#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  string S,T,ans="Yes";
  int s,t;
  cin >> S >> T;
  int A[26], B[26], L;
  for (int i = 0; i < 26; ++i) {
    A[i] = -1;
    B[i] = -1;
  }

  L = S.length();
  for (int i = 0; i < L; ++i) {
    s = static_cast<int>(S[i]-'a');
    t = static_cast<int>(T[i]-'a');
    if (A[s] == -1 && B[t] == -1) {
      A[s] = t;
      B[t] = s;
    }else if (A[s] == t && B[t] == s) {
      continue;
    }else {
      ans = "No";
    }
  }
  cout << ans << "\n";
  return 0;
}
