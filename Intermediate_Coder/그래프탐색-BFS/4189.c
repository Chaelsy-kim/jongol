#include <stdio.h>
int a[2] = { 0 };
int b[2] = { 0 };
int n, m;
int v[8][2] = {
    {-1,-2},
    {-1,2},
    {1,-2},
    {1,2},
    {2,1},
    {2,-1},
    {-2,-1},
    {-2,1}
};
int stack[10000000][2] = { 0 };
int visited[1001][1001] = { 0 };
int top = -1;
int rear = -1;
 
int find(int x, int y) {
    int i, p, q;
    int z = visited[x][y] + 1;
    if (x == b[0] && y == b[1]) {
        printf("%d", visited[x][y]);
        return 0;
    }
    for (i = 0; i < 8; i++) {
        p = x + v[i][0];
        q = y + v[i][1];
        if (p< 1 || p > n || q < 1 || q > m || visited[p][q] <= z)
            continue;
        stack[++top][0] = p;
        stack[top][1] = q;
        visited[p][q] = z;
    }
    rear++;
    find(stack[rear][0], stack[rear][1]);
}
 
int main() {
    int i, j;
    scanf("%d %d", &n, &m);
    scanf("%d %d %d %d", &a[0], &a[1], &b[0], &b[1]);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
            visited[i][j] = 1000000;
    visited[a[0]][a[1]] = 0;
    find(a[0], a[1]);
    return 0;
 
}
