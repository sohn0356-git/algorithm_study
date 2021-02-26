#include <iostream>
using namespace std;

int T;
int A, B;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		cin >> A >> B;
		cout << "Case #" << tc << ": " << A + B << '\n';
	}
	return 0;
}