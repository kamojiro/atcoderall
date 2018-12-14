#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int N, M, X, Y;
  cin >> N >> M >> X >> Y;
  int x[N], y[M];
  for (int i = 0; i < N; ++i) {
    cin >> x[i];
  }
  for (int i = 0; i < M; ++i) {
    cin >> y[i];
  }
  for (int i = 0; i < N; ++i) {
    if (X < x[i]) X = x[i];
  }
  for (int i = 0; i < M; ++i) {
    if (Y > y[i]) Y = y[i];
  }
  if (X < Y) {
    cout << "No War" << "\n";
  }
  else {
    cout << "War" << "\n";
  }

  return 0;
}
