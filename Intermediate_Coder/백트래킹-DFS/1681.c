#include <stdio.h>
int a[12][12] = { 0 };
int v[12] = { 0 };
int n, ans = 100000, temp = 0;
int stack[1000][2] = { 0 };
int top = -1;
int d[1000][2] = { 0 };
int z = -1;

int find(int x) {
	int i, p=0, q=0, y = 0, count = 0;

	for (i = n - 1; i >= 0; i--) {
		if (a[x][i] == 0 || v[i] == 1)
			continue;
		stack[++top][0] = x;
		stack[top][1] = i;
		y++;
	}

	if(y!=0){
		p = stack[top][0];
		q = stack[top][1];
		top--;
		v[p] = 1;
		d[++z][0] = p;
		d[z][1] = q;
		temp += a[p][q];
	}
	if (y == 0 || temp>ans) {
		
		if (z==n-2 && a[x][0]!=0) {
			if (ans > temp + a[x][0])
				ans = temp + a[x][0];
		}
		p = stack[top][0];
		q = stack[top][1];
		if (top <= -1)
			return 0;

		temp += a[p][q];
		top--;

		while (d[z][0] != p) {
			v[d[z][0]] = 0;
			temp -= a[d[z][0]][d[z][1]];
			z--;	
		}
		temp -= a[d[z][0]][d[z][1]];
		d[z][0] = p;
		d[z][1] = q;
		
	}
	
	find(q);
}

int main() {
	int i, j;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			scanf("%d", &a[i][j]);

	find(0);
	printf("%d", ans);
}
