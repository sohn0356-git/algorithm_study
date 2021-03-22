#include <iostream>

using namespace std;

long long A, B, C;
long long solve(long long b);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> A >> B >> C;
	cout << solve(B);
	return 0;
}

long long solve(long long b)
{
	if (b == 0)
	{
		return 1LL;
	}
	if (b == 1)
	{
		return A % C;
	}
	if (b % 2 == 0)
	{
		long long temp = solve(b / 2);
		return ((temp%C)*(temp%C)) % C;
	}
	else
	{
		return (A*solve(b - 1))%C;
	}
}