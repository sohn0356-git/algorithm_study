#include <iostream>
#include <string>

using namespace std;

int N, M, K;
int DP[101][101];
int solve(int a, int z);
string word(int a, int z, int idx);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M >> K;
	for (int i = 0; i < 101; i++)
	{
		for (int j = 0; j < 101; j++)
		{
			DP[i][j] = -1;
		}
	}
	int len = solve(N, M);
	if (K > len)
	{
		cout << -1;
	}
	else
	{
		cout << word(N, M, K);
	}
	return 0;
}


int solve(int a, int z)
{
	if (a == 0 || z == 0)
	{
		return 1;
	}
	int& res = DP[a][z];
	if (res != -1)
	{
		return res;
	}
	res = min(solve(a - 1, z) + solve(a, z - 1), 1000000000);
	return res;
}

string word(int a, int z, int idx)
{
	string ret = "";
	if (a == 0)
	{
		for (int i = 0; i < z; i++)
		{
			ret += "z";
		}
		return ret;
	}
	if (z == 0)
	{
		for (int i = 0; i < a; i++)
		{
			ret += "a";
		}
		return ret;
	}
	int a_start = solve(a - 1, z);
	if (a_start < idx)
	{
		return "z" + word(a, z - 1, idx - a_start);
	}
	else
	{
		return "a" + word(a - 1, z, idx);
	}
}