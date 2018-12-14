#include <bits/stdc++.h>
#define all(v) v.begin(),v end()
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
const ll INF = 1000000010;
const ll LINF = 4000000000000000000LL;
typedef pair<int, int> P;

signed main(){
  int a, b, c;
  cin >> a >> b >> c;
  cout << max({a * 10 + b + c, a + b * 10 + c,a + b + c * 10}) << endl;
}