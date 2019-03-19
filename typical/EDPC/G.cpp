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
  int N, M, x, y, s, z;
  cin >> N >> M;
  vector<int> E[N];
  int V[N];
  for (int i = 0; i < N; ++i) {
    V[i] = 1;
  }

  for (int i = 0; i < M; ++i) {
    cin >> x >> y;
    x--; y--;
    V[y] = 0;
    E[x].push_back(y);
  }
  vector<int> S;
  int Pathdistance[N];
  for (int i = 0; i < N; ++i) {
    Pathdistance[i] = -1;
  }

  for (int i = 0; i < N; ++i) {
    if (V[i] == 1) {
      S.push_back(i);
    }
  }
  while (S.size()) {
    s = S.back();
    S.pop_back();
    Pathdistance[s] = 0;
    int now = 1;
    vector<int> Z;
    for (unsigned int i = 0; i < E[s].size(); ++i) {
      if (Pathdistance[E[s][i]] < now) {
        Z.push_back(E[s][i]);
        Pathdistance[E[s][i]] = now;
      }
    }
    while (Z.size()) {
      vector<int> T(0,0);
      now++;
      int t = Z.size();
      for (unsigned int i = 0; i < t; ++i) {
        z = Z.back();
        Z.pop_back();
        int s = E[z].size();
        for (unsigned int j = 0; j < E[z].size(); ++j) {
          if (Pathdistance[E[z][j]] < now) {
            T.push_back(E[z][j]);
            Pathdistance[E[z][j]] = now;
          }
        }
      }
      Z = T;
    }
  }
  int ans = 0;
  for (int i = 0; i < N; ++i) {
    if (ans < Pathdistance[i]){
      ans = Pathdistance[i];
    }
  }
  cout << ans << "\n";
  return 0;
}
