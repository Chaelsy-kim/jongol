#include <stdio.h>
char a[51][51] = { 0 };
int b[51][51] = { 0 };
int queue[10000][2] = { 0 };
int top = -1;
int rear = -1;
int queue1[10000][2] = { 0 };
int top1 = -1;
int rear1 = -1;
int n, m;
int check;

int v[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};
int find(int s, int t, int x, int y) {
    int i, j, p, q, g, h;
    int z1, z2;
    int temp1 = b[s][t], temp2 = b[x][y];
    z1 = b[s][t] - 1;
    z2 = b[x][y] + 1;

    while (z1 != temp1) {
        if (s == 50 && t == 50)
            break;
        for (i = 0; i < 4; i++) {
            g = s + v[i][0];
            h = t + v[i][1];
            if (g < 0 || g >= n || h < 0 || h >= m)
                continue;
            if (a[g][h] == 'X' || a[g][h] == 'D')
                continue;
            if (b[g][h] >= z1 && b[g][h] < 0)
                continue;
            queue[++top][0] = g;
            queue[top][1] = h;
            b[g][h] = z1;
        }
        rear++;
        s = queue[rear][0];
        t = queue[rear][1];
        temp1 = b[s][t];
        
    }

    while (z2 != temp2) {
        for (i = 0; i < 4; i++) {
            p = x + v[i][0];
            q = y + v[i][1];
            if (p < 0 || p >= n || q < 0 || q >= m)
                continue;
            if (a[p][q] == '*' || a[p][q] == 'X')
                continue;
            if (b[p][q] <= z2 && b[p][q] != 0)
                continue;
            queue1[++top1][0] = p;
            queue1[top1][1] = q;
            b[p][q] = z2;

            if (a[p][q] == 'D') {
                check = 1;
                return 0;
            }
        }
        if (rear1 > top1) {
            printf("impossible");
            check = 0;
            return 0;
        }
        rear1++;
        x = queue1[rear1][0];
        y = queue1[rear1][1];
        temp2 = b[x][y];
    }

    find(s, t, x, y);

}

int main() {
    int i, j, p, q, s = 50, t = 50, max = 0;
    char c;
    scanf("%d %d", &n, &m);

    for (i = 0; i < n; i++)
        scanf("%s", a[i]);

    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++) {
            if (a[i][j] == '*') {
                b[i][j] = -1;
                queue[++top][0] = i;
                queue[top][1] = j;
                s = i;
                t = j;
            }
            else if (a[i][j] == 'S') {
                b[i][j] = 1;
                queue1[++top1][0] = i;
                queue1[top1][1] = j;
                p = i;
                q = j;
            }
        }
  
    find(s, t, p, q);

    if (check == 1) {
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++) {
                if (max < b[i][j])
                    max = b[i][j];
            }
        printf("%d", max - 1);
    }

}
