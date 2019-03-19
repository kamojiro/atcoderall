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
  int N,x;
  vector<int> Z;
  cin >> N;
  for (int i = 0; i < N; ++i) {
    cin >> x;
    Z.push_back(x);
  }
  cout << Z.size() << "\n";
  for (int i = 0; i < N; ++i) {
    x = Z.back();
    cout << x << "\n";
    Z.pop_back();
  }
  cout << Z.size() << "\n";
  return 0;
}
