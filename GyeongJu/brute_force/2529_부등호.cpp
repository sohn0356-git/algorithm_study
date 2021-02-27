#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N;
char tmp;
string maxV = "";
string minV = "";
int arr[10] = { 9,8,7,6,5,4,3,2,1,0 };
int used[10];
int comb[10];

vector<char> order;
void solve(int stage, int dir);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> tmp;
		order.push_back(tmp);
	}
	solve(0, 0);
	for (int i = 0; i < 10; i++)
	{
		used[i] = 0;
		arr[i] = i;
	}
	solve(0, 1);
	cout << maxV << '\n' << minV;

	return 0;
}

void solve(int stage, int dir)
{
	if (maxV != "" && dir == 0)
	{
		return;
	}
	if (minV != "" && dir == 1)
	{
		return;
	}
	if (stage == N + 1)
	{
		string val = "";
		for (int i = 0; i < N; i++)
		{
			if (order[i] == '<' && comb[i] < comb[i + 1])
			{
				val += to_string(comb[i]);
			}
			else if(order[i]=='>' && comb[i] > comb[i+1])
			{
				val += to_string(comb[i]);
			}
			else
			{
				return;
			}
		}
		val += to_string(comb[N]);
		if (dir == 0)
		{
			maxV = val;
		}
		else
		{
			minV = val;
		}
		return;
	}
	for (int i = 0; i < 10; i++)
	{
		if (used[i] == 0)
		{
			used[i] = 1;
			comb[stage] = arr[i];
			solve(stage + 1,dir);
			used[i] = 0;
		}
	}
}