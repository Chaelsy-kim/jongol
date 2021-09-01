#include <stdio.h>
#include <stdlib.h>
int a[100][100] = { 0 };
int c[4];
int m, n, k, i, j, x;
int b[10000] = { 0 };
int top = -1;
int ans = 0;
int search(int x, int y) {
	if (a[x][y] == 1) {
		ans++;
		a[x][y] = 0;
		if (y != n - 1)
			search(x, y + 1);
		if (y != 0)
			search(x, y - 1);
		if (x != 0)
			search(x - 1, y);
		if (x != m - 1)
			search(x + 1, y);
	}
	else {
		return 0;
	}
}

void clean() {
	int i = top - 1, j = top;
	int temp;
	while (b[i] > b[j]) {
		temp = b[j];
		b[j] = b[i];
		b[i] = temp;
		j--;
		i--;
	}
}

int main() {
	int t = 0;
	scanf("%d %d %d", &m, &n, &k);

	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
			a[i][j] = 1;

	for (i = 0; i < k; i++) {
		scanf("%d %d %d %d", &c[0], &c[1], &c[2], &c[3]);
		for (j = c[0]; j < c[2]; j++)
			for (x = c[1]; x < c[3]; x++)
				a[x][j] = 0;
	}

	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			if (a[i][j] == 1){
				search(i, j);
				b[++top] = ans;
				clean();
				ans = 0;
				t++;
			}
		}
	}

	printf("%d\n", t);
	for (i = 0; i <= top; i++)
		printf("%d ", b[i]);	
}
