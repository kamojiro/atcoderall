#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()

// struct Compare
// {
//   constexpr bool operator()(pair<int, int> const &a, pair<int, int> const) const noexcept
//   {return a.first < b.first;}
// };

int main()
{
  int N;
  cin >> N;
  int A[N];
  int B[N];
  //  priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> q;
  priority_queue<pair<int, int>> q;
  for (int i = 0; i < N; ++i) {
    cin >> A[i];
  }
  for (int i = 0; i < N; ++i) {
    cin >> B[i];
    q.push( make_pair(B[i], i));
  }
  // for (int i = 0; i < N; ++i) {
  //   cout << q.top().first << "\n";
  //   q.pop();
  // }
  ll ans = 0;
  int check = 0;
  pair<int, int> now;
  int i, a;
  while (check < N) {
    now = q.top();
    q.pop();
    a = now.first;
    i = now.second;
    //    cout << a << " " << i << "\n";
    if (B[i] == A[i]) {
      check++;
      continue;
    }
    ans++;
    a = a - B[(N+(i-1))%N] - B[(i+1)%N];
    B[i] = a;
    if (B[i] == A[i]) {
      check++;
    }else if (B[i] > A[i]) {
      q.push(make_pair(a, i));
    }else {
      ans = -1;
      break;
    }
  }
  cout << ans << "\n";
  return 0;
}
