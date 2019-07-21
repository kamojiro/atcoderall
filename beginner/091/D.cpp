#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
#include <math.h>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()
int main()
{
  int N;
  ll a, t, now;
  int p;
  cin >> N;
  vector<int> vecA;
  vector<int> vecB;
  for (int i = 0; i < N; ++i) {
    cin >> a;
    vecA.push_back(a);
  }
  for (int i = 0; i < N; ++i) {
    cin >> a;
    vecB.push_back(a);
  }
  vector<int> check(N);
  int ans[30];
  for (int i = 0; i < 30; ++i) {
    now = 0;
    t = pow(2,i);
    for (int j = 0; j < N; ++j) {
      check[j] = vecA[j]%(2*t);
    }
    sort(all(check));
    for (int j = 0; j < N; ++j) {
      a = vecB[j]%(t*2);
      now += (lower_bound(all(check),t*2-a) - lower_bound(all(check), t-a)) + (lower_bound(all(check), 4*t-a) - lower_bound(all(check), t*3-a));
    }
    ans[i] = now%2;
  }
  ll ret = 0;
  for (int i = 0; i < 30; ++i) {
    ret += ans[i]*pow(2,i);
  }
  cout << ret << "\n";
  return 0;
}
