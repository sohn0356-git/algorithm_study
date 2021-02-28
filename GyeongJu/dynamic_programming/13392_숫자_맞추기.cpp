#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int N;
string M, K;
int DP[10001][10];
int solve(int stage, int cum);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	for (int i = 0; i < 10001; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			DP[i][j] = -1;
		}
	}
	cin >> N >> M >> K;
	cout << solve(0, 0);
	return 0;
}

int solve(int stage, int cum)
{
	if (stage == N)
	{
		return 0;
	}
	int& res = DP[stage][cum];
	if (res != -1)
	{
		return res;
	}
	int ms = M[stage] - '0';
	int ks = K[stage] - '0';
	ms += cum;
	ms %= 10;
	int sub = ks - ms;
	//turn left
	if (sub < 0)
	{
		sub += 10;
	}
	int tl = sub + solve(stage + 1, (cum + sub) % 10);
	//turn right
	sub = ms - ks;
	if (sub < 0)
	{
		sub += 10;
	}
	int tr = sub + solve(stage + 1, cum);	
	res = min(tr, tl);
	return res;
}