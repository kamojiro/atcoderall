#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
  int N, i, j, min = 1000;
  cin >> N;
  for (i = 0; i < N; ++i) {
    int a;
    scanf("%d", &a);
    for (j=0; !(a%2); ++j) a /= 2;
    if (min > j) {
      min = j;
        };
  }
  cout << min << "\n";
  return 0;
}
