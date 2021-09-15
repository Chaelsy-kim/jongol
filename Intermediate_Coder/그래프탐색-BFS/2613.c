#include <stdio.h>
int a[1001][1001] = { 0 };
int queue[1000000][2] = { 0 };
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

int find(int x, int y) {
    int i, j, p, q;
    int z = a[x][y] + 1;
    
    if (rear > top) {
        return 0;
    }

    for (i = 0; i < 4; i++) {
        p = x + v[i][0];
        q = y + v[i][1];
        if (p < 1 || p>n || q<1 || q>m)
            continue;
        if (a[p][q] <= z && a[p][q] !=0)
            continue;
        queue[++top][0] = p;
        queue[top][1] = q;
        a[p][q] = z;
    }
    rear++;
    find(queue[rear][0], queue[rear][1]);
}

int main() {
    int i, j, p, q, max = 0,empty=0;
    scanf("%d %d", &m, &n);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
            scanf("%d", &a[i][j]);

    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++) {
            if (a[i][j] == 1) {
                queue[++top][0] = i;
                queue[top][1] = j;
            }
            else if (a[i][j] == -1)
                empty++;
        }
            
    if (n * m==empty+rear) {
        printf("%d", 0);
        return 0;
    } 
    else {
        rear++;
        find(queue[rear][0], queue[rear][1]);
    }

    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++) {
            if (max < a[i][j])
                max = a[i][j];
            if (a[i][j] == 0) {
                printf("%d", -1);
                return 0;
            }
        }

    printf("%d", max-1);
}
