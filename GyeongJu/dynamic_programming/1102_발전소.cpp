#include <iostream>
#include <memory.h>

#define Max 17
#define INF 987654321
#define min(a,b) (a<b)?a:b

using namespace std;

int N,bm,P,onC;
int arr[Max][Max];
int DP[Max][1<<Max];


int solve(int cnt, int on);


int main()
{
	memset(DP, -1, sizeof(DP));
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> arr[i][j];
		}
	}
	for (int i = 0; i < N; i++)
	{
		char c;
		cin >> c;
		if (c == 'Y')
		{
			onC++;
			bm |= (1 << i);
		}
	}
	cin >> P;
	int ans = solve(onC, bm);
	if (ans == INF)
		cout << -1;
	else
		cout << ans;
	return 0;
}


int solve(int cnt, int on)
{
	if (cnt >= P)
		return 0;
	int &ret = DP[cnt][on];
	if (ret != -1)
		return ret;
	ret = INF;
	for (int i = 0; i < N; i++)
	{
		if (on&(1 << i))
		{
			for (int j = 0; j < N; j++)
			{
				if (on&(1 << j)) continue;
				ret = min(ret, solve(cnt + 1, on | (1 << j))+arr[i][j]);
			}
		}
	}
	return ret;
}