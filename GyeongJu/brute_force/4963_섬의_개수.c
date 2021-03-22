#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int w, h, cnt;
int arr[51][51];
int visited[51][51];
int dirR[8] = { -1,-1,0,1,1,1,0,-1 };
int dirC[8] = { 0,1,1,1,0,-1,-1,-1 };

void dfs(int r, int c);

int main()
{
	while (1)
	{
		cnt = 0;
		scanf("%d %d", &w, &h);
		if (w == 0 && h == 0)
		{
			break;
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &arr[i][j]);
				visited[i][j] = 0;
			}
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (visited[i][j] == 0 && arr[i][j] == 1)
				{
					cnt++;
					dfs(i, j);
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}

void dfs(int r, int c)
{
	visited[r][c] = cnt;
	for (int d = 0; d < 8; d++)
	{
		int nR = r + dirR[d];
		int nC = c + dirC[d];
		if (nR >= 0 && nR < h && nC >= 0 && nC < w) 
		{
			if (visited[nR][nC] == 0 && arr[nR][nC] == 1)
			{
				dfs(nR, nC);
			}
		}
	}
}#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int w, h, cnt;
int arr[51][51];
int visited[51][51];
int dirR[8] = { -1,-1,0,1,1,1,0,-1 };
int dirC[8] = { 0,1,1,1,0,-1,-1,-1 };

void dfs(int r, int c);

int main()
{
	while (1)
	{
		cnt = 0;
		scanf("%d %d", &w, &h);
		if (w == 0 && h == 0)
		{
			break;
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &arr[i][j]);
				visited[i][j] = 0;
			}
		}
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (visited[i][j] == 0 && arr[i][j] == 1)
				{
					cnt++;
					dfs(i, j);
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}

void dfs(int r, int c)
{
	visited[r][c] = cnt;
	for (int d = 0; d < 8; d++)
	{
		int nR = r + dirR[d];
		int nC = c + dirC[d];
		if (nR >= 0 && nR < h && nC >= 0 && nC < w) 
		{
			if (visited[nR][nC] == 0 && arr[nR][nC] == 1)
			{
				dfs(nR, nC);
			}
		}
	}
}