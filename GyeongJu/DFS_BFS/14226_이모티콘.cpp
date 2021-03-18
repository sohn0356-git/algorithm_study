#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;


int S, ans;
int dist[1001][1001];
queue<pair<int,int>> q;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	memset(dist, -1, sizeof(dist));
	cin >> S;
	q.push({ 1,0 });
	dist[1][0] = 0;
	while (!q.empty())
	{
		int nS = q.front().first;
		int nC = q.front().second;
		q.pop();
		if (dist[nS][nS] == -1)
		{
			dist[nS][nS] = dist[nS][nC] + 1;
			q.push({ nS, nS });
		}
		if (nS+nC<=S && dist[nS+nC][nC] == -1)
		{
			dist[nS+nC][nC] = dist[nS][nC] + 1;
			q.push({ nS+nC, nC });
		}
		if (nS-1>=0 && dist[nS-1][nC] == -1)
		{
			dist[nS-1][nC] = dist[nS][nC] + 1;
			q.push({ nS-1, nC });
		}
	}
	int ans = -1;
	for (int i = 0; i <= S; i++) {
		if (dist[S][i] != -1) {
			if (ans == -1 || ans > dist[S][i]) {
				ans = dist[S][i];
			}
		}
	}
	cout << ans << '\n';
	return 0;
}