#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, T, M;
int t1, t2;
int graph[501][501];
int indegree[501];
int visited[501];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		for (int i = 0; i < 501; i++)
		{
			indegree[i] = 0;
			visited[i] = 0;
			for (int j = 0; j < 501; j++)
			{
				graph[i][j] = 0;
			}			
		}
		vector<int>ans;
		cin >> N;
		cin >> t1;
		visited[t1]++;
		for (int i = 1; i < N; i++)
		{
			cin >> t2;
			for (int j = 1; j <= N; j++)
			{
				if (visited[j] == 1)
				{
					graph[t2][j] = 1;
					indegree[t2]++;
				}
			}
			visited[t2]++;
			t1 = t2;
		}
		cin >> M;
		for (int i = 0; i < M; i++)
		{
			cin >> t1 >> t2;
			if (graph[t1][t2] == 1)
			{
				graph[t2][t1] = 1;
				graph[t1][t2] = 0;
				indegree[t2]++;
				indegree[t1]--;
			}
			else
			{
				graph[t1][t2] = 1;
				graph[t2][t1] = 0;
				indegree[t1]++;
				indegree[t2]--;
			}
		}
		queue<int>q;
		for (int i = 1; i <= N; i++)
		{
			if (indegree[i] == 0)
			{
				q.push(i);
			}
		}
		while (!q.empty())
		{
			int cur = q.front();
			q.pop();
			ans.push_back(cur);
			for (int i = 1; i <= N; i++)
			{
				if (graph[i][cur] == 1)
				{
					indegree[i]--;
					if (indegree[i] == 0)
					{
						q.push(i);
					}
				}
			}
		}
		if (ans.size() != N)
		{
			cout << "IMPOSSIBLE\n";
		}
		else
		{
			for (int i = 0; i < ans.size(); i++)
			{
				cout << ans[i] << ' ';
			}
			cout << '\n';
		}
	}

	return 0;
}