#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

int N;
int arr[10001];
int DP[10001][2];

int solve(int stage, int eat);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	memset(DP, -1, sizeof(DP));
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	cout<<solve(0,0);

	return 0;
}

int solve(int stage, int eat)
{
	if (stage >= N)
	{
		return 0;
	}
	int &res = DP[stage][eat];
	if (res != -1)
	{
		return res;
	}
	res = 0;
	if (eat==0)
	{
		res = max(res, solve(stage + 1, 0));
		res = max(res, arr[stage]+solve(stage+1,1));
	}
	else
	{
		res = max(res, solve(stage + 1, 0));
		res = max(res, arr[stage]+solve(stage + 2, 0));
	}
	return res;
}