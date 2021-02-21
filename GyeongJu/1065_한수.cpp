//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int N, ans;
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cin >> N;
//	for (int i = 1; i <= N; i++)
//	{
//		string str_i = to_string(i);
//		bool flag = true;
//		for (int j = 0; j < (int)(str_i.length())-2; j++)
//		{
//			if (str_i[j] - str_i[j + 1] != str_i[j + 1] - str_i[j + 2])
//			{
//				flag = false;
//				break;
//			}
//		}
//		if (flag)
//		{
//			ans++;
//		}
//	}
//	cout << ans;
//	return 0;
//}