#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(){
  int n, q;
  cin >> n >> q;
  dsu d(n);
  for (int i = 0; i < q; ++i) {
    int t, u, v;
    cin >> t >> u >> v;
    if (t == 0) {
      d.merge(u,v);
    }else{
      if (d.same(u,v)){
        cout << 1 << "\n";
      }else{
        cout << 0 << "\n";
      }
    }
  }
  return 0;
}
