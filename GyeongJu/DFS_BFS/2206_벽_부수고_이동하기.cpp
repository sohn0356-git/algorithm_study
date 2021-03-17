#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct Info {
	int r;
	int c;
	int b;
	Info(int _r, int _c, int _b) :r(_r), c(_c), b(_b) {}
};


int N, M;
string maze[1001];
int visited[2][1001][1001];
int dirR[4] = { 1,0,-1,0 };
int dirC[4] = { 0,1,0,-1 };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		cin >> maze[i];
	}

	queue<Info>q;
	q.push(Info(0,0,0));
	visited[0][0][0] = 1;

	while (!q.empty())
	{
		Info cur = q.front();
		q.pop();
		for (int d = 0; d < 4; d++)
		{
			int nR = cur.r + dirR[d];
			int nC = cur.c + dirC[d];
			if (nR >= 0 && nR < N && nC >= 0 && nC < M)
			{
				if (cur.b == 0)
				{
					if (visited[1][nR][nC]==0 && maze[nR][nC] == '1')
					{
						visited[1][nR][nC] = visited[0][cur.r][cur.c] + 1;
						q.push(Info(nR, nC, 1));
					}
				}
				if (visited[cur.b][nR][nC] == 0 && maze[nR][nC] == '0')
				{
					visited[cur.b][nR][nC] = visited[cur.b][cur.r][cur.c] + 1;
					q.push(Info(nR, nC, cur.b));
				}
			}
		}
	}
	int ans = -1;
	//int ans = (visited[0][N - 1][M - 1] < visited[1][N - 1][M - 1]) ? visited[0][N - 1][M - 1] : visited[1][N - 1][M - 1];//삼항연산자
	if (visited[0][N - 1][M - 1] == 0 && visited[1][N - 1][M - 1] == 0)
	{
		ans = -1;
	}
	else if (visited[0][N - 1][M - 1] != 0 && visited[1][N - 1][M - 1] != 0)
	{
		ans = (visited[0][N - 1][M - 1] < visited[1][N - 1][M - 1]) ? visited[0][N - 1][M - 1] : visited[1][N - 1][M - 1];//삼항연산자
	}
	else
	{
		ans = (visited[0][N - 1][M - 1] > visited[1][N - 1][M - 1]) ? visited[0][N - 1][M - 1] : visited[1][N - 1][M - 1];//삼항연산자
	}
	cout << ans;
	return 0;
}