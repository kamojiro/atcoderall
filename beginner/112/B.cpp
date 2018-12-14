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
  int N, T, time, cost;
  cin >> N >> T;
  int C[N], M[N];
  for (int i = 0; i < N; ++i) {
    cin >> C[i] >> M[i];
  }

  time = T+1;
  cost = 1001;
  for (int i = 0; i < N; ++i) {
    if (M[i] <= T) {
      if (C[i] < cost) {
        cost = C[i];
        time = 0;
      }
    }
  }
  if (time == T+1) {
    cout << "TLE" << "\n";
  }else {
    cout << cost << "\n";
  }

  return 0;
}
