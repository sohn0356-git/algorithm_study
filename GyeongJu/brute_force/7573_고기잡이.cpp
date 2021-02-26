#include <iostream>
#include <vector>

using namespace std;


int N, I, M, t1, t2, ans;
vector<pair<int, int>> v;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> I >> M;
	for (int i = 0; i < M; i++)
	{
		cin >> t1 >> t2;
		v.push_back({ t1,t2 });
	}
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 0; j < v.size(); j++)
		{
			int r = v[i].first;
			int c = v[j].second;

			for (int l = 1; l < I / 2; l++)
			{
				//l : 세로, m : 가로
				int m = I / 2 - l;
				if (l < N && m < N)
				{
					while (r + l > N)
					{
						r--;
					}
					while(c + m > N)
					{
						c--;
					}
					int cnt = 0;
					for (int k = 0; k < v.size(); k++)
					{
						if (v[k].first >= r && v[k].first <= r + l && v[k].second >= c && v[k].second <= c + m)
						{
							cnt++;
						}
					}
					if (ans < cnt)
					{
						ans = cnt;
					}
				}
			}
		}
	}
	cout << ans;


	return 0;
}