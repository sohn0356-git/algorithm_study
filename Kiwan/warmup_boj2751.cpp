#include <iostream>
using namespace std;

void mergeSort(int *, int *, int, int);

int main(void) {
	int N;

	cin >> N;
	int * arrN = new int[N];
	int * temp = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> *(arrN + i);
	}

	mergeSort(arrN, temp, 0, N-1);
	for (int i = 0; i < N; i++) {
		cout << *(arrN + i) << " ";
	}
	cout << endl;

	delete[]arrN;
	delete[]temp;
	return 0;
}
void mergeSort(int * arr, int * temp, int left, int right)
{
	if (left == right)
		return;
	int mid = (left + right) / 2;

	mergeSort(arr, temp, left, mid);
	mergeSort(arr, temp, mid + 1, right);

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right) {
		if (arr[i] < arr[j]) {
			temp[k] = arr[i];
			i++, k++;
		}
		else {
			temp[k] = arr[j];
			j++, k++;
		}
	}

	while (i <= mid) {
		temp[k] = arr[i];
		i++, k++;
	}
	while (j <= right) {
		temp[k] = arr[j];
		j++, k++;
	}

	for (int l = left; l <= right; l++) {
		arr[l] = temp[l];
	}
		
}