#include <iostream>

using namespace std;

int N;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = N - 1 - i; j > 0; j--)
		{
			cout << ' ';
		}
		for (int j = 0; j < 2 * i + 1; j++)
		{
			cout << '*';
		}
		cout << '\n';
	}
	return 0;
}