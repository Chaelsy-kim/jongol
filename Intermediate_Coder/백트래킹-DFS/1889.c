#include <stdio.h>

int a[14][14] = { 0 };
int top[14] = { 0 };
int i = 1;

void push(int x) {
    a[i][top[i]++] = x;
}

int pop() {
    if (top[i] == 0)
        return -1;
    else
        return a[i][--top[i]];
}

int main() {
    int x[30] = { 0 };
    int b[30] = { 0 };
    int n, j, s, k, y = 0;
    int ans = 0;

    scanf("%d", &n);
    for (j = n; j >= 1; j--) 
        push(j);
      
    if (n == 1)
        ans = 1;
    x[i] = pop();
    i++;
    while (i <= n) {
        for (j = 1; j < i; j++) {
            if (x[j] - (i - j) < 1) {
                b[x[j]] = 1;
                b[x[j] + (i - j)] = 1;
            }
            else if (x[j] + (i - j) > n) {
                b[x[j]] = 1;
                b[x[j] - (i - j)] = 1;
            }
            else {
                b[x[j]] = 1;
                b[x[j] + (i - j)] = 1;
                b[x[j] - (i - j)] = 1;
            }
        }

        for (j = n; j >= 1; j--) {
            if (b[j] == 0) {
                push(j);  
            }
        }
        k = pop();
        if (k != -1){
            x[i] = k;
            i++;
            if (i > n) {
                ans++;
                i--;
                k = pop();
                while (k == -1) {
                    if (i == 1) {
                        y = 1;
                        break;
                    }
                    i--;
                    k = pop();
                }
                if (y == 1)
                    break;
                x[i] = k;
                i++;
            }
        }
        else{
            i--;
            k = pop();
            while (k == -1) {
                if (i == 1) {
                    y = 1;
                    break;
                }   
                i--;
                k = pop();
            }
            if (y == 1)
                break;
            x[i] = k;
            i++;
        }
        for (s = 1; s <= n; s++) {
            b[s] = 0;
        }
    }

    printf("%d", ans);

}
