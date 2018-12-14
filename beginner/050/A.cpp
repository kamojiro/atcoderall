#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int a, b;
  char op;
  cin >> a >> op >> b;
  if (op == '+') {
    //    printf("%d\n", a+b);
    cout << a+b << "\n";
  }else {
    cout << a-b << "\n";
    //printf("%d\n", a-b);
  }
  return 0;
}
