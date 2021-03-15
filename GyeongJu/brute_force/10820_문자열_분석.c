#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	char test[101];
	int answer[4] = { 0, };
	while (fgets(test,sizeof(test), stdin) != NULL) {
		int idx = 0;
		while (1) {
			if (test[idx] == '\0')
			{
				break;
			}
			if (test[idx] >= 'a' && test[idx] <= 'z')
			{
				answer[0]++;
			}
			else if (test[idx] >= 'A' && test[idx] <= 'Z')
			{
				answer[1]++;
			}
			else if (test[idx] >= '0' && test[idx] <= '9')
			{
				answer[2]++;
			}
			else if(test[idx]==' ')
			{
				answer[3]++;
			}
			idx++;
		}
		if (idx == 1)
		{
			continue;
		}
		for (int i = 0; i < 4; i++)
		{
			printf("%d ", answer[i]);
			answer[i] = 0;
		}
		printf("\n");		
	}
	return 0;
}