#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <sstream>
#include <iterator>

using namespace std;

class SegmentTree{
  vector<int> tree;
  vector<int> array;
  vector<int> left, right;
  int n;

  void makeTree(int i){
    if(i >= n - 1){
      tree[i] = array[i - n + 1];
      left[i] = i - n + 1;
      right[i] = left[i] + 1;
    }
    else{
      makeTree(2 * i + 1);
      makeTree(2 * i + 2);
      tree[i] = min(tree[2 * i + 1], tree[2 * i + 2]);
      left[i] = left[2 * i + 1];
      right[i] = right[2 * i + 2];
    }
  }

  int getMin(int i, int l, int r){
    int ret;
    if(l >= right[i] || r <= left[i]) ret = INT_MAX;
    else if(l <= left[i] && right[i] <= r) ret = tree[i];
    else ret = min(getMin(2 * i + 1, l, r), getMin(2 * i + 2, l, r));
    return ret;
  }

public:
  SegmentTree(const vector<int>& a){
    int m = 1;
    while(m < (int)a.size()){
      m *= 2;
    }
    n = (int)a.size();

    array.resize(m, INT_MAX);
    copy(a.begin(), a.end(), array.begin());

    tree.resize(2 * m - 1);
    left.resize(2 * m - 1);
    right.resize(2 * m - 1);
    makeTree(0);
  }

  int getMin(int l, int r){
    return getMin(0, l, r);
  }

  void debug(){
    copy(tree.begin(), tree.end(), ostream_iterator<int>(cout, " ")); cout << endl;
    copy(array.begin(), array.end(), ostream_iterator<int>(cout, " ")); cout << endl;
  }
};

int main(int argc, char* argv[]){
  stringstream sst(argv[1]);
  int buf;
  vector<int> a;
  while(sst >> buf){
    a.push_back(buf);
  }
  SegmentTree st(a);
  cout << st.getMin(atoi(argv[2]), atoi(argv[3])) << endl;
  st.debug();

  return 0;
}


