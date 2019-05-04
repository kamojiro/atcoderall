#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()

int main()
{
  int H, W;
  cin >> H >> W;
  string A[H];
  for (int i = 0; i < H; ++i) {
    cin >> A[i];
  }
  int B[H][W];
  queue<int> q;
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (A[i][j] == '#') {
        B[i][j] = 0;
        q.push(i*W+j);
      }else {
        B[i][j] = -1;
      }
    }
  }
  int t,h,w;
  while (!q.empty()) {
    t = q.front();
    q.pop();
    h = t/W;
    w = t - h*W;
    if (h > 0){
      if (B[h-1][w] == -1){
        B[h-1][w] = B[h][w]+1;
        q.push((h-1)*W+w);
      }
    }
    if (h < H -1){
      if (B[h+1][w] == -1){
        B[h+1][w] = B[h][w]+1;
        q.push((h+1)*W+w);
      }
    }
    if (w > 0){
      if (B[h][w-1] == -1){
        B[h][w-1] = B[h][w]+1;
        q.push(h*W+w-1);
      }
    }
    if (w < W -1){
      if (B[h][w+1] == -1){
        B[h][w+1] = B[h][w]+1;
        q.push(h*W+w+1);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (B[i][j] > ans) {
        ans = B[i][j];
      }
    }
  }
  cout << ans << "\n";
  return 0;
}
