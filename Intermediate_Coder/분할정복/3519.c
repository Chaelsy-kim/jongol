#include <stdio.h>

int a[1000] = { 0 };
int b[1000] = { 0 };
int n;

void mergeSort(low, high) {
	
	if (low >= high) {

	}
	else {
		int mid = (low + high) / 2;

		mergeSort(low, mid);
		mergeSort(mid + 1, high);

		int i = low, j = mid + 1;
		for (int k = low; k <= high; k++) {
			if (j > high)
				b[k] = a[i++];
			else if (i > mid)
				b[k] = a[j++];
			else if (a[i] < a[j])
				b[k] = a[i++];
			else
				b[k] = a[j++];
		}

		for (i = low; i <= high; i++)
			a[i] = b[i];

		for (i = 0; i < n; i++)
			printf("%d ", a[i]);
		printf("\n");

	}
	
}

int main() {
	
	int i;
	scanf("%d", &n);
	int low = 0, high = n - 1;
	
	for (i = 0; i < n; i++)
		scanf("%d", &a[i]);

	mergeSort(low, high);
	
}
