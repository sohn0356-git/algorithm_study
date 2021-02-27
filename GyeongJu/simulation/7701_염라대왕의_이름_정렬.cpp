#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int T, N;
string tmp;

bool compare(string s1, string s2);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		cin >> N;
		vector<string>name;
		for (int i = 0; i < N; i++)
		{
			cin >> tmp;
			name.push_back(tmp);
		}
		sort(name.begin(), name.end(),compare);
		cout <<"#"<<tc<<'\n'<< name[0] << '\n';
		for (int i = 1; i < N; i++)
		{
			if (name[i] == name[i - 1])
			{
				continue;
			}
			cout << name[i] << '\n';
		}
	}

	return 0;
}

bool compare(string s1, string s2)
{
	if (s1.length() == s2.length())
	{
		for (int i = 0; i < s1.length(); i++)
		{
			if (s1[i] == s2[i])
			{
				continue;
			}
			return s1[i] < s2[i];
		}
	}
	else
	{
		return s1.length() < s2.length();
	}
}