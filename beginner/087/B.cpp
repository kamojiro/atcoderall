#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int A, B, C, X, ans=0, i, j, k;
  cin >> A;
  cin >> B;
  cin >> C;
  cin >> X;
  for (i = 0; i <= A; ++i) {
    for (j = 0; j <= B; ++j) {
      for (k = 0; k <= C; ++k) {
        if (500*i + 100*j + 50*k == X) ans++;
      }      
    }
  }
  cout << ans << "\n";
  return 0;
}
