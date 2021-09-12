#include <stdio.h>
int a[101][101] = { 0 };
int queue[1000][2] = { 0 };
int top = -1;
int rear = -1;
int n, m;
int ans;
int v[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};
int find(int x,int y) {
    int i,j, p, q;
    int z = a[x][y] + 1;
 
    if (rear > top) {
        return 0;
    }
         
    for (i = 0; i < 4; i++) {
        p = x + v[i][0];
        q = y + v[i][1];
        if (p < 1 || p>n || q<1 || q>m )
            continue;
        if (a[p][q] < z && a[p][q] != 1)
            continue;
        queue[++top][0] = p;
        queue[top][1] = q;
        a[p][q] = z;
    }
    rear++;
    find(queue[rear][0], queue[rear][1]);
}
 
int main() {
    int i, j, p, q, max=0, ans = 0;
    scanf("%d %d", &m, &n);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
            scanf("%1d", &a[i][j]);
    scanf("%d %d", &q, &p);
    a[p][q] = 3;
    find(p, q);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++) {
            if (max < a[i][j])
                max = a[i][j];
            if (a[i][j] == 1)
                ans++;
        }
    printf("%d\n%d", max, ans);
}
