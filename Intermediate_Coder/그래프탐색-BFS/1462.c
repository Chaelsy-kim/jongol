#include <stdio.h>
char a[100][100] = { 0 };
int b[100][100] = { 0 };
int queue[10000][2] = { 0 };
int top = -1;
int rear = -1;
int n, m;

int v[4][2] = {
	{1,0},
	{-1,0},
	{0,1},
	{0,-1}
};
int find(int x,int y) {
	int i,j, p, q;
	int z = b[x][y] + 1;
	
	if (rear > top) {
		return 0;
	}
		
	for (i = 0; i < 4; i++) {
		p = x + v[i][0];
		q = y + v[i][1];
		if (p < 0 || p >= n || q < 0 || q >= m)
			continue;
		if (b[p][q] <= z && b[p][q] != 1)
			continue;
		queue[++top][0] = p;
		queue[top][1] = q;
		b[p][q] = z;
	}
	rear++;
	find(queue[rear][0], queue[rear][1]);
}

int main() {
	int i, j, p, q, max = 0;
	char c;
	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%s", a[i]);
		
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			if (a[i][j] == 'L')
				b[i][j] = 1;	
	
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++) {
			if (b[i][j] == 1) {
				b[i][j] = 2;
				find(i, j);
				for (p = 0; p < n; p++)
					for (q = 0; q < m; q++)
						if (max < b[p][q])
							max = b[p][q];
				for (p = 0; p < n; p++)
					for (q = 0; q < m; q++)
						if (a[p][q] == 'L')
							b[p][q] = 1;
				top = -1;
				rear = -1;
			}
		}
	
	printf("%d", max-2);
	
}
