#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
#include<complex>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<bitset>
using namespace std;
#define REP(i,m,n) for(int i=(int)m ; i < (int) n ; ++i )
#define rep(i,n) REP(i,0,n)
typedef long long ll;
typedef pair<int,int> pint;
typedef pair<ll,int> pli;
const int inf=1e9+7;
const ll longinf=1LL<<60 ;
const ll mod=1000003 ;
 
ll dp[5050],dp2[25000001];
ll w[5],w2[5];
ll v[5],v2[5];

int main(){
  ll n;
  cin >> n;
  ll a[2][3];
  rep(i,2){
    rep(j,3)cin >> a[i][j];
  }
  rep(i,3){
    w[i]=a[0][i];
    v[i]=a[1][i];
    w2[i]=a[1][i];
    v2[i]=a[0][i];
  }
  v[3]=1;
  w[3]=1;
  v2[3]=1;
  w2[3]=1;
  for(int i=0;i<4;i++){
    for(int j=0;j<=n;j++){
      if(j<w[i]){
        dp[j]=dp[j];
      }else{
        dp[j]=max(dp[j],dp[j-w[i]]+v[i]);
      }
    }
  }
  ll m=dp[n];
  for(int i=0;i<4;i++){
    for(int j=0;j<=m;j++){
      if(j<w2[i]){
        dp2[j]=dp2[j];
      }else{
        dp2[j]=max(dp2[j],dp2[j-w2[i]]+v2[i]);
      }
    }
  }
  cout << dp2[m] << endl;
return 0;}
