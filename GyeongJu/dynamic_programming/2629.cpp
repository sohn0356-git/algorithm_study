#include <iostream>
#include <algorithm>

using namespace std;

int num_w;
int weight[31];
int num_q;
int q;
int DP[31][80001];
char answer[2] = { 'N', 'Y' };

int solve(int num, int w);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> num_w;
	
	for (int i = 0; i < num_w; i++)
	{
		cin >> weight[i];
	}
	sort(weight, weight + num_w);
	cin >> num_q;
	for (int i = 0; i < num_q; i++)
	{
		for (int j = 0; j < 31; j++)
		{
			for (int k = 0; k < 80001; k++)
			{
				DP[j][k] = -1;
			}
		}
		cin >> q;
		cout << answer[solve(0, 40000+q)]<< ' ';
	}

	return 0;
}

int solve(int num, int w)
{
	if (w == 40000)
	{
		return 1;
	}
	if (num >= num_w)
	{
		return 0;
	}
	int& res = DP[num][w];
	if (res != -1)
	{
		return res;
	}
	res = 0;
	res |= solve(num + 1, w);
	res |= solve(num + 1, w + weight[num]);
	res |= solve(num + 1, w - weight[num]);
	return res;
}
