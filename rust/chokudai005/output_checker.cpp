#include "testlib.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main(int argc, char* argv[])
{
	setName("chokudai005");
	registerTestlibCmd(argc, argv);

	try {
		int id, N, K;
		id = inf.readInt(1, 50);
		inf.readSpace();
		N = inf.readInt(100, 100);
		inf.readSpace();
		K = inf.readInt(9, 9);
		inf.readEoln();
		
		vector<vector<int>> color(N, vector<int>(N, 0));

		for(int i = 0; i < N; i++){
			string S = inf.readWord();
			ensure(S.size() == N);

			for(int j = 0; j < N; j++){
				color[i][j] = S[j] - '0';
				ensure(color[i][j] >= 1);
				ensure(color[i][j] <= 9);
			}
			inf.readEoln();
		}
		inf.readEof();

		int Q = ouf.readInt(0, 10000);
		for (int i = 0; i < Q; i++)
		{
			int Y = ouf.readInt(1, N) - 1;
			int X = ouf.readInt(1, N) - 1;
			int C = ouf.readInt(1, K);

			int FirstC = color[Y][X];

			if(C == FirstC) continue;

			queue<pair<int, int>> q;
			q.push(make_pair(Y, X));
			color[Y][X] = C;
			
			vector<int> vy = {1, 0, -1, 0};
			vector<int> vx = {0, 1, 0, -1};
			while(!q.empty()){
				auto now = q.front(); q.pop();
				int nowY = now.first;
				int nowX = now.second;

				for(int k = 0; k < 4; k++){
					int nextY = nowY + vy[k];
					int nextX = nowX + vx[k];
					if(nextY < 0 || nextY >= N) continue;
					if(nextX < 0 || nextX >= N) continue;
					if(color[nextY][nextX] == FirstC){
						color[nextY][nextX] = C;
						q.push(make_pair(nextY, nextX));
					}
				}
			}
		}
		
		int point = 0;
		for(int i = 1; i <= K; i++){
			int cnt = 0;
			for(int y = 0; y < N; y++){
				for(int x = 0; x < N; x++){
					if(color[y][x] == i) cnt++;
				}
			}
			point = max(point, cnt);
		}
		point *= 100;
		point -= Q;

		cout << "IMOJUDGE<<<" << point << ">>>" << endl;
		quitf(_ok, "Accept");
	}
	catch (exception e) {
		cout << "IMOJUDGE<<<0>>>" << endl;
		quitf(_wa, "Something wrong");
	}
	return 0;

}
