#include <iostream>
#include <stack>
using namespace std;

int N;
int arr[500001];
stack<int> lastMaxIdx;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	
	for (int i = 1; i <= N; i++)
	{
		cin >> arr[i];
		if (arr[i] < arr[i - 1])
		{
			lastMaxIdx.push(i - 1);
			cout << i - 1 << ' ';
		}
		else
		{
			while (!lastMaxIdx.empty())
			{
				if (arr[i] < arr[lastMaxIdx.top()])
				{
					cout << lastMaxIdx.top() << ' ';
					break;
				}
				else
				{
					lastMaxIdx.pop();
				}
			}
			if (lastMaxIdx.empty())
			{
				cout << 0 << ' ';
			}
		}
	}

	return 0;
}