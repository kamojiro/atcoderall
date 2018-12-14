#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int SIZ = 100;
int r, c;
char maz[SIZ + 5][SIZ + 5];
bool pri[SIZ + 5];
int main()
{
  scanf("%d%d", &r, &c);
  int cnt = 0;
  for (int i = 0; i < r; i++)
  {
    bool flag = false;
    scanf("%s", maz[cnt]);
    for (int j = 0; j < c;j++)
      if (maz[cnt][j] == '#')
        flag = true, pri[j] = true;
    if(flag)
      cnt++;
  }

  for (int i = 0; i < cnt;i++)
  {
    for (int j = 0; j < c;j++)
      if (pri[j])
        printf("%c", maz[i][j]);
    printf("\n");
  }
  return 0;
}
