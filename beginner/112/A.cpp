#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
  int Q;
  cin >> Q;
  //if Q == 1
  if (Q==1) {
    std::cout << "Hello World" << "\n";
  }
  else if (Q==2){
    int A, B;
    cin >> A >> B;
    int ans = A+B;
    std::cout << ans << "\n";
  }
  return 0;
}

