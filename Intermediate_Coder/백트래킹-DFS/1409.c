#include <stdio.h>
#include <stdlib.h>
 
int a[20] = { 0 };
int b[2] = { 0 };
int c[2] = { 0 };
int x, y, i, ans = 0, temp=1000;
 
int fun(int i,int j) {
    int num = ans;
    int t[2] = { b[0],b[1] };
    if (j == y) {
        if (temp > ans)
            temp = ans;
        return 0;
    }
    if (b[0] <= a[j] && b[1] <= a[j]) {
        ans += a[j] - b[1];
        b[1] = a[j];
    }
    else if (b[0] >= a[j] && b[1] >= a[j]) {
        ans += b[0] - a[j];
        b[0] = a[j];
    }
    else {
        ans += abs(a[j] - b[i]);
        b[i] = a[j];
    }
     
    fun(0, j + 1);
    fun(1, j + 1);
    ans = num;
    b[0] = t[0];
    b[1] = t[1];
     
}
 
int main() {
 
    scanf("%d", &x);
    scanf("%d %d", &c[0], &c[1]);
    scanf("%d", &y);
    for (i = 0; i < y; i++)
        scanf("%d", &a[i]);
     
    b[0] = c[0];
    b[1] = c[1];
    fun(0, 0);
 
    ans = 0;
    b[0] = c[0];
    b[1] = c[1];
    fun(1, 0);
        
    printf("%d", temp);
     
}
