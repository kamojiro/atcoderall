#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()
int main()
{
  int N, l;
  cin >> N;
  string w, x, y, ans = "Yes", W[N];
  cin >> w;
  W[0] = w;
  for (int i = 1; i < N; ++i) {
    cin >> x;
    if (w[ w.size() - 1] == x[0]) {
      ;
    }else {
      ans = "No";
    }
    for (int j = 0; j < i; ++j) {
      if (x == W[j]) {
        ans = "No";
      }
    }
    W[i] = x;
    w = x;
    }
  cout << ans << "\n";
  return 0;
}
