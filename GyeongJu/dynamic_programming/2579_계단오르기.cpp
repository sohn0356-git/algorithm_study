#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>

using namespace std;


int arr[300];
int DP[10001][2];       // 0 밟은 거 1 안 밟은 거


int main()
{

		int N;
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			cin >> arr[i];
		}

		DP[1][0] = arr[0];
		DP[2][0] = arr[0]+arr[1];
		DP[2][1] = arr[1];
		for (int i = 3; i <= N; i++)
		{
			DP[i][0] = arr[i - 1] + DP[i - 1][1];
			DP[i][1] = arr[i - 1] + ((DP[i - 2][1]>DP[i - 2][0]) ? DP[i - 2][1] : DP[i - 2][0]); 
		}
		int ans = (DP[N][0] > DP[N][1]) ? DP[N][0] : DP[N][1];
		cout << ans;

	return 0;
}
