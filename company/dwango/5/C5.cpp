#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()

int main()
{
  int N, Q;
  string S;
  cin >> N >> S >> Q;
  int K[Q];
  for (int i = 0; i < Q; ++i) {
    cin >> K[i];
  }
  for (int i = 0; i < Q; ++i) {
    long long k = K[i], D=0, M=0, DM=0, ans=0;
    for (int j = 0; j < k; ++j) {
      if (S[j] == 'D') {
        D++;
      }else if (S[j] == 'M') {
        M++;
        DM += D;
      }else if (S[j] == 'C') {
        ans += DM;
      }
    }
    for (int j = k; j < N; ++j) {
      //まずは取り除くことから
      if (S[j-k] == 'D') {
        D--;
        DM -= M;
      }else if (S[j-k] == 'M') {
        M--;
      }
      if (S[j] == 'D') {
        D++;
      }else if (S[j] == 'M') {
        M++;
        DM += D;
      }else if (S[j] == 'C') {
        ans += DM;
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
