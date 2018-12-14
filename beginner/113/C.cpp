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
  int n, m;
  cin >> n >> m;
  vector<pair<pair<int,int>, int>>city(m);
  vector<pair<int,int>>ans(m);
  int y[n];
  for (int i = 0; i < n; ++i) {
    y[i] = 0;
  }

  for (int i = 0; i < m; ++i) {
    cin >> city[i].first.second >> city[i].first.first;
    city[i].second = i;
  }
  sort(all(city));
  for (int i = 0; i < m; ++i) {
    y[city[i].first.second-1] += 1;
    ans[city[i].second].first = city[i].first.second;
    ans[city[i].second].second = y[city[i].first.second-1];
  }
  for (int i = 0; i < m; ++i) {
    printf("%06d%06d\n", ans[i].first, ans[i].second);
  }

  return 0;
}
