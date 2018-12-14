#include <iostream>
using namespace std;
int main(){
  int N;
  cin >> N;
  int ans = 0;
  for (int C = 1; C <= N;C+=2){
    int div = 0;
    for (int X = 1; X <= C;++X){
      if (C%X==0){
        ++div;
      }
    }
    if (div == 8 ){
      ++ans;
    }
  }
  cout << ans << '\n';
  return 0;
}