#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
#include <deque>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()

int main()
{
  int N, M, x, y, s, l;
  cin >> N >> M;
  int V[N];
  vector<int> E[N], T;
  deque<int> S;
  for (int i = 0; i < N; ++i) {
    V[i] = 0;
  }
  for (int i = 0; i < M; ++i) {
    cin >> x >> y;
    x--; y--;
    E[x].push_back(y);
    V[y] += 1;
  }
  for (int i = 0; i < N; ++i) {
    if (V[i] == 0) {
      S.push_back(i);
    }
  }

  while (S.size()) {
    s = S[0];
    S.pop_front();
    T.push_back(s);
    l = E[s].size();
    for (int i = 0; i < l; ++i) {
      V[E[s][i]]--;
      if (V[E[s][i]] == 0) {
        S.push_back(E[s][i]);
      }
    }
  }
  int ANS[N];
  for (int i = 0; i < N; ++i) {
    ANS[i] = 0;
  }
  int v, t;
  for (int i = 0; i < N; ++i) {
    v = T[i];
    t = ANS[v] + 1;
    l = E[v].size();
    for (int j = 0; j < l; ++j) {
      if (t > ANS[E[v][j]]) {
        ANS[E[v][j]] = t;
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < N; ++i) {
    if (ans < ANS[i]) {
      ans = ANS[i];
    }
  }
  cout << ans << "\n";
  return 0;
}

