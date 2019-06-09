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
  int H, W;
  cin >> H >>W;
  vector<string> P(H);
  int T[H][W];
  int Y[H][W];
  int S[H][W];
  for (int i = 0; i < H; ++i) {
    cin >> P[i];
  }
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (P[i][j] == '#') {
        S[i][j] = 1;
      }else{
        S[i][j] = 0;
      }
    }

  }

  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      T[i][j] = 1;
      Y[i][j] = 1;
    }

  }

  int now, cnt;
  for (int i = 0; i < H; ++i) {
    now = 0;
    cnt = 0;
    for (int j = 0; j < W; ++j) {
      if (S[i][j] == 0){
      cnt += 1;
    }else{
      for (int k = now; k < j; ++k) {
        T[i][k] = cnt;
      }
      cnt = 0;
      now = j+1;
    }
    if (cnt > 0) {
      for (int k = now; k < W; ++k) {
        T[i][k] = cnt;
      }
    }
  }
  }
  for (int i = 0; i < W; ++i) {
    now = 0;
    cnt = 0;
    for (int j = 0; j < H; ++j) {
      if (S[j][i] == 0){
      cnt += 1;
    }else{
      for (int k = now; k < j; ++k) {
        Y[k][i] = cnt;
      }
      cnt = 0;
      now = j+1;
    }
    if (cnt > 0) {
      for (int k = now; k < H; ++k) {
        Y[k][i] = cnt;
      }
    }
  }
  }
  int ans = 0;
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (ans < T[i][j] + Y[i][j]-1) {
        ans = T[i][j] + Y[i][j]-1;
      }
    }
  }
  cout << ans << "\n";
  return 0;
}
