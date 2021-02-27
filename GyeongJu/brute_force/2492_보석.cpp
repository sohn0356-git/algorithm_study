//#include <iostream>
//#include <vector>
//#include <map>
//
//using namespace std;
//
//int N, M, T, K, t1, t2;
//
//pair<int, pair<int, int>>ans;
//vector<pair<int, int>>v;
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cin >> N >> T >> K;
//	for (int i = 0; i < T; i++)
//	{
//		cin >> t1 >> t2;
//		v.push_back({ t2,t1 });
//	}
//	ans.second = { N,0 };
//	for (int i = 0; i < v.size(); i++)
//	{
//		for (int j = 0; j < v.size(); j++)
//		{
//			int ni = v[i].first;
//			int nj = v[j].second;
//			if (ni - K < 0)
//			{
//				ni = K;
//			}
//			if (nj + K > M)
//			{
//				nj = M - K;
//			}
//
//			int cnt = 0;
//			for (int k = 0; k < v.size(); k++)
//			{
//				if (v[k].first <= ni && v[k].first >= ni - K && v[k].second >= nj && v[k].second <= nj + K)
//				{
//					cnt++;
//				}
//			}
//			if (ans.first < cnt)
//			{
//				ans.first = cnt;
//				ans.second = { ni, nj };
//			}
//
//		}
//	}
//	cout << ans.second.second << ' ' << ans.second.first << '\n';
//	cout << ans.first;
//	return 0;
//}