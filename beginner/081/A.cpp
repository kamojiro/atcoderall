#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
  char S[3];
  int ans = 0;
  int i;
  scanf("%s", S);
  for (i = 0; i<3; ++i) {
    if (S[i] == '1') {
      ans++;
        };
  }
  cout << ans << "\n";
  return 0;
}
