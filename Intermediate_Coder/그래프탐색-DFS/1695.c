#include <stdio.h>
#include <stdlib.h>
char a[25][25] = { 0 }; 
int b[10000] = { 0 };
int top = -1;
int ans = 0;
int n, i, j;

int search(int x,int y) {
	if (a[x][y] == '1') {
		ans++;
		a[x][y] = 0;
		if(y!=n-1)
			search(x, y+1);
		if(y!=0)
			search(x, y - 1);
		if(x!=0)
			search(x - 1, y);
		if(x!=n-1)
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
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%s", &a[i]);	

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (a[i][j] == '1')
				search(i, j);
			if (ans != 0) {
				b[++top] = ans;
				clean();
				ans = 0;
				t++;
			}
		}
	}
	printf("%d\n", t);
	for (i = 0; i <= top; i++)
		printf("%d\n", b[i]);
}
