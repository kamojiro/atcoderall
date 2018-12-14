#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int N, A, B, ans = 0, i, j;
  cin >> N >> A >> B;
  for (i = 1; i <= N; ++i) {
    int wa = 0;
    j = i;
    while (j != 0){
      wa += j%10;
      j /= 10;
    }
    if (A <= wa && wa <= B) ans += i;
  }
  cout << ans  << "\n";
  return 0;
}
