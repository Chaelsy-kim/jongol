#include <stdio.h>
int a[100000] = { 0 };
int b[100000] = { 0 };
int top = 0;
int rear = 0;
int i, s = 0, x;
int last=0;
int temp[100000] = { 0 };
int y[100000] = { 0 };

int pop() {
    return a[rear++];
}

void push(int x) {
    a[top++] = x;
}

void func() {
    while (a[rear] < x) {
        if (rear == top)
            break;
        b[s++] = i + 1;
        pop();
    }
    push(x);
}

int main() {

    int n, k, p;
    
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &x);

        if (top == rear)
            push(x);
        else {
            if (a[rear] >= x) {
                if (a[top-1] >= x)
                    push(x);
                else {
                    while (a[rear] >= x) {
                        temp[last] = a[rear];
                        y[last++] = s++;
                        pop();
                    }
                    func();
                }
            }
            else {
                p = -1;
                if (last != 0) {
                    for (k = last - 1; k >= 0; k--) {
                        if (temp[k] < x) {
                            b[y[k]] = i + 1;
                            temp[k] = 0;
                            
                            p = k;
                        }
                        else
                            break;
                    }
                }
                if(p!=-1)
                    last = p;
                func();
            }
        }
        
    }
    for (i = 0; i < n; i++)
        printf("%d\n", b[i]);

    return 0;
}
