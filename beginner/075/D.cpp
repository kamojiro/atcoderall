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
  int N, K;
  cin >> N >> K;
  int X[N], Y[N], SX[N], SY[N];
  ll a, b, c, d, ans;
  ans = LLONG_MAX;
  for (int i = 0; i < N; ++i) {
    cin >> X[i] >> Y[i];
    SX[i] = X[i];
    SY[i] = Y[i];
  }
  sort(SX, SX+N);
  sort(SY, SY+N);
  for (int i = 0; i < N-1; ++i) {
    a = SX[i];
    for (int j = i+1; j < N; ++j) {
      b = SX[j];
      for (int k = 0; k < N-1; ++k) {
        c = SY[k];
        for (int l = k+1; l < N; ++l) {
          d = SY[l];
          int cnt=0;
          for (int m=0; m < N; ++m) {
            if ((a <= X[m]) and (X[m] <= b) and (c <= Y[m]) and ( Y[m] <= d)) {
              cnt++;
            }
          if (cnt >= K) {
            if ((b-a)*(d-c) < ans) {
              ans = (b-a)*(d-c);
            }
          }
          }

        }

      }

    }

      
  }
  cout << ans << "\n";
  return 0;
}
