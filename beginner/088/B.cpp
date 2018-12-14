#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int N, i, k, A=0, B=0, ans;
  cin >> N;
  char a[N];
  for (i = 0; i < N; ++i) {
    scanf("%d", &a[i]);
  }
  sort(a, a+N);
  if ((N-1)%2 == 0) {
    k=0;
  } else {
    k = 1;
  }
  for (i = N-1; i >= 0; --i) {
    if (i%2 == k) {
      A += a[i];
    }    else {
      B += a[i];
    }
  }
  ans = A - B;
  cout << ans << "\n";
  return 0;
}


