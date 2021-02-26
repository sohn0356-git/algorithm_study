#include <iostream>
using namespace std;
int tmp;
char name[5] = { 'D','C','B','A','E' };

int main()
{
	for (int i = 0; i < 3; i++)
	{
		int sum = 0;
		for (int j = 0; j < 4; j++)
		{
			cin >> tmp;
			sum += tmp;
		}
		cout << name[sum] << '\n';
	}
	return 0;
}