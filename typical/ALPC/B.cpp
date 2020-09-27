#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(){
  // int n, m;
  // cin >> n >> m;
  int N, Q;
  cin >> N >> Q;
  fenwick_tree<long long> fw(N);

  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    fw.add(i,a);
  }

  for (int i = 0; i < Q; ++i) {
    int q;
    cin >> q;
    if (q == 0) {
      int p, x;
      cin >> p >> x;
      fw.add(p, x);
    }else{
      int l, r;
      cin >> l >> r;
      cout << fw.sum(l,r) << "\n";
    }
  }
  return 0;
}
