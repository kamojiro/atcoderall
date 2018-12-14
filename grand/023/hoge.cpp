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
  ll a=0, N=8100000000;
  for (int i = 0; i < N; ++i) {
    a += 1;
  }
  cout << a << "\n";
  return 0;
}
