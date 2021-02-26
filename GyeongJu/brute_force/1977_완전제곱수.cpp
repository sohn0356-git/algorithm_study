#include <iostream>

using namespace std;

int M, N, ans, minV;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> M >> N;
	for (int i = M; i <= N; i++)
	{
		for (int j = 1; j * j <= i; j++)
		{
			if (j * j == i)
			{
				if (ans == 0)
				{
					minV = i;
				}
				ans += i;
			}
		}
	}
	if (ans == 0)
	{
		cout << -1;
	}
	else
	{
		cout << ans << '\n';
		cout << minV;
	}

	return 0;
}