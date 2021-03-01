#include <iostream>

using namespace std;

int M, N;
int arr[501][501];
int DP[501][501];

int dirR[4] = { 1,0,-1,0 };
int dirC[4] = { 0,1,0,-1 };

int solve(int r, int c);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> arr[i][j];
			DP[i][j] = -1;
		}
	}
	cout << solve(0, 0);
	return 0;
}


int solve(int r, int c)
{
	if (r == N - 1 && c == M - 1)
	{
		return 1;
	}
	int& res = DP[r][c];
	if (res != -1)
	{
		return res;
	}
	res = 0;
	for (int d = 0; d < 4; d++)
	{
		int nR = r + dirR[d];
		int nC = c + dirC[d];
		if (nR >= 0 && nR < N && nC >= 0 && nC < M)
		{
			if (arr[r][c] > arr[nR][nC])
			{
				res += solve(nR, nC);
			}
		}
	}
	return res;
}