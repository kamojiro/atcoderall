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
  cin >> N;
  cin >> S;
  cin >> Q;
  int K[Q];
  for (int i=0; i < Q; ++i) {
    cin >> K[i];
  }
  int dp[N+1][3];
  for (int i=0; i < N+1; ++i) {
    for (int j=0; i < 3; ++j) {
      dp[i][j] = 0
    }
  }
  for (int i=0; i < N; ++i) {
    for (j=0; j < 3; ++j) {
      dp[i+1][j] = dp[i][j]
    }

    if (S[i]=="D") {
      dp[i+1][0] = dp[i][0]+1;
    }else if (S[i] == "M") {
      dp[i+1][1] = dp[i][0] + dp[i][1];
    }else if (S[i] == "C") {
      dp[i+1][2] = dp[i][1] + dp[i][2];
    }
  }
  for (int i = 0; i < Q; ++i) {
    
  }


  return 0;
}
