//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int N;
//int arr[501][501];
//int DP[501][501];
//int dirR[4] = { -1,0,1,0 };
//int dirC[4] = { 0,1,0,-1 };
//
//int solve(int r, int c);
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cin >> N;
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < N; j++)
//		{
//			cin >> arr[i][j];
//			DP[i][j] = -1;
//		}
//	}
//	int ans = 0;
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < N; j++)
//		{
//			ans = max(ans, solve(i, j));
//		}
//	}
//	cout << ans;
//	return 0;
//}
//
//int solve(int r, int c)
//{
//	int& res = DP[r][c];
//	if (res != -1)
//	{
//		return res;
//	}
//	res = 1;
//	for (int d = 0; d < 4; d++)
//	{
//		int nR = r + dirR[d];
//		int nC = c + dirC[d];
//		if (nR >= 0 && nR < N && nC >= 0 && nC < N)
//		{
//			if (arr[r][c] < arr[nR][nC])
//			{
//				res = max(res, 1 + solve(nR, nC));
//			}
//		}
//	}
//	return res;
//}