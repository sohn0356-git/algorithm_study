#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int T, N, K, X, Y, W;
long long D;
int indegree[1001];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		vector<long long>cTime;
		queue<pair<int,int>>q;
		cTime.push_back(0);
		vector<int>graph[1001];
		long long time[1001];
		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			time[i + 1] = 0;
			indegree[i + 1] = 0;
			cin >> D;
			cTime.push_back(D);
		}
		for (int i = 0; i < K; i++)
		{
			cin >> X >> Y;
			indegree[Y]++;
			graph[X].push_back(Y);
		}
		cin >> W;
		for (int i = 1; i <= N; i++)
		{
			if (indegree[i] == 0)
			{
				q.push({ i,0 });
				time[i] = cTime[i];
			}
		}
		while (!q.empty())
		{
			pair<int, int>cur = q.front();
			q.pop();
			for (int i = 0; i < graph[cur.first].size(); i++)
			{
				int next = graph[cur.first][i];
				indegree[next]--;
				if (time[next] < time[cur.first] + cTime[next])
				{
					time[next] = time[cur.first] + cTime[next];
				}
				if (indegree[next] == 0)
				{
					q.push({ next,cur.second + 1 });
				}
			}
		}
		cout << time[W] << '\n';
	}
	return 0;
}