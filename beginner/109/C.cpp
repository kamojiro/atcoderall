#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()
int main()
{
  int N, t, ans, s;
  cin >> N >> t;
  int x[N];
  for (int i = 0; i < N; ++i) {
    cin >> x[i];
  }
  ans = abs(t-x[0]);
  for (int i=0; i < N; ++i) {
    s = ans;
    ans = __gcd(s, abs(t-x[i]));
  }
  cout << ans << "\n";
  return 0;
}
