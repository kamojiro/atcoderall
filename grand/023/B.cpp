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
  int N, ans=0;
  cin >> N;
  string S[N];
  bool check;
  for (int i = 0; i < N; ++i) {
    cin >> S[i];
  }
  // for (int i = 0; i < N; ++i) {
  //   for (int j = 0; j < N; ++j) {
  //     cout << S[i][j] << "\n";
  //   }

  // }

  for (int k = 0; k < N; ++k) {
    check = 1;
    for (int i = 0; i < N && check == 1 ; ++i) {
      for (int j = i+1; j < N && check == 1; ++j) {
        if (!( S[i][(j+k)%N] == S[j][(i+k)%N])) {
          check = 0;
          // cout << i << j << "\n";
        }
      }
    }
    if (check == 1) {
      ans += N;
    } 
  }
  cout << ans << "\n";

  return 0;
}
