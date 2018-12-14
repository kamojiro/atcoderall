#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long int ll;

int main()
{
  int N, T, A, i, ans = 1;
  cin >> N >> T >> A;
  int H[N];
  T *= 1000;
  A *= 1000;
  for (i = 0; i < N; ++i) {
    cin >> H[i];
    H[i] = abs(T-H[i]*6-A);
  }
  int now = H[0];
  for (i = 0; i < N; ++i) {
    if ( H[i] < now) {
      now = H[i];
      ans = i+1;
    }
  }
  cout << ans << "\n";
  return 0;
}
