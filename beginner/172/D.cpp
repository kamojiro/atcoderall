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
  int n;
  ll ans=0;
  cin >> n;
  n++;
  vector<ll> Ints(n);
  for (int i = 0; i < n; ++i) {
    Ints[i] = i;
  }
  vector<ll> Factors(n);
  for (int i = 0; i < n; ++i) {
    Factors[i] = 1;
  }

  for (int i = 2; i < n; ++i) {
    if (Ints[i] == 1){
      continue;
      }
    for (int j = 1; j < n; ++j) {
      if (i*j < n) {
        ll t = 1;
        while (Ints[i*j]%i == 0) {
          Ints[i*j] = Ints[i*j]/i;
          t += 1;
        }
        Factors[i*j] = Factors[i*j]*t;
      }
      else{
        break;
      }
    }
  }
  // for (int i = 0; i < n; ++i) {
  //   cout << "F" <<i << Factors[i] << "\n";
  // }

  for (int i = 1; i < n; ++i) {
    ans = ans + i*Factors[i];
  }
  cout << ans << "\n";

  return 0;
}
