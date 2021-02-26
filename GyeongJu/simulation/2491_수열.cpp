#include <iostream>

using namespace std;

int N, tmp;
int arr[100001];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int start(0), end(0), ans(1);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	//증가
	for (int i = 1; i < N; i++)
	{
		if (arr[i] < arr[i - 1])
		{
			if (ans < end - start + 1)
			{
				ans = end - start + 1;
			}
			start = i;
			end = i;
		}
		else
		{
			end++;
		}
	}
	if (ans < end - start + 1)
	{
		ans = end - start + 1;
	}
	start = 0;
	end = 0;
	//감소
	for (int i = 1; i < N; i++)
	{
		if (arr[i] > arr[i - 1])
		{
			if (ans < end - start + 1)
			{
				ans = end - start + 1;
			}
			start = i;
			end = i;
		}
		else
		{
			end++;
		}
	}
	if (ans < end - start + 1)
	{
		ans = end - start + 1;
	}
	cout << ans;

	return 0;
}