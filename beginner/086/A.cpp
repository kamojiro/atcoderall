#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
  int a, b;
  cin >> a >> b;
  if (a%2 == 1 && b%2 == 1) {
    cout << "Odd" << "\n";
  }
  else {
    cout << "Even" << "\n";
  }
  return 0;
}
