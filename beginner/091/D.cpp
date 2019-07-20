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
  int N, a, now, t;
  cin >> N;
  vector<int> vec;
  for (int i = 0; i < N; ++i) {
    cin >> a;
    vec.push_back(a);
  }
  vector<int> check(N);
  int[] ans = int[30];
  for (int i = 0; i < 30; ++i) {
    now = 0;
    t = 2**i;
    for (int j = 0; j < N; ++j) {
      check[j] = vec[j]%(2*t);
    }
    sort(check.all);
    for (int j = 0; j < N; ++j) {
      check[j] = A[j]%(t*2);
      now += (lower_bound(all(check),t*2-a) - bisect_left(D, t-a)) + (bisect_left(D, 4*t-a) - bisect_left(D, t*3-a))
    }
    sort(all(check));
    
         

  }

  return 0;
}
