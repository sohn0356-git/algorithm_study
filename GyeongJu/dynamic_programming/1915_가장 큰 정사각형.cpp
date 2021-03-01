#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int N, M, ans;
string arr[1001];
int DP[1001][1001];
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
		cin >> arr[i];
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < arr[i].length(); j++)
		{
			if (arr[i][j] == '1')
			{
				if (i - 1 >= 0 && j - 1 >= 0)
				{
					DP[i][j] = min(DP[i - 1][j], min(DP[i - 1][j - 1], DP[i][j - 1])) + 1;
				}
				else
				{
					DP[i][j] = 1;
				}
				if (ans < DP[i][j])
				{
					ans = DP[i][j];
				}
			}
		}
	}
	cout << ans;

	return 0;
}
