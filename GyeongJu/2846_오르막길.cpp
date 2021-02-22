#include <iostream>

using namespace std;

int N;
int ans, cnt;
int arr[1001];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	cin >> arr[0];
	for (int i = 1; i < N; i++)
	{
		cin >> arr[i];
		if (arr[i - 1] >= arr[i])
		{
			if (ans < arr[i - 1] - arr[cnt])
			{
				ans = arr[i - 1] - arr[cnt];
			}
			cnt = i;
		}
	}
	if (ans < arr[N - 1] - arr[cnt])
	{
		ans = arr[N - 1] - arr[cnt];
	}
	cout << ans;
	return 0;
}