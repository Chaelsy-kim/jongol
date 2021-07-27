#include <stdio.h>
int a[500000] = { 0 };
int b[500000] = { 0 };
int c[500000] = { 0 };
int temp[500000] = { 0 };
int y[500000] = { 0 };
int last = -1;
int i, s = 0, x, n;
int top = 0;
int rear = 0;

void push(int x) {
    temp[++last] = x;
}

int pop() {
    return temp[last--];
}

int dequeue() {
    return a[rear++];
}
void enqueue(int x) {
    a[top++] = x;
}

void func() {
    while (a[rear] < x) {
        if (rear == top)
            break;
        c[s++] = n - i;      
        dequeue();
    }
    enqueue(x);
}

int main() {
    scanf("%d", &n);

    for (i = n-1; i >= 0; i--) 
        scanf("%d", &b[i]);

    for (i = 0; i <n; i++) {
        x = b[i];

        if (top == rear)
            enqueue(x);
        else {
            if (a[rear] >= x) {
                if (a[top - 1] >= x)
                    enqueue(x);
                else {
                    while (a[rear] >= x) {
                        push(a[rear]);
                        y[last] = s++;
                        dequeue();
                    }
                    func();
                }
            }
            else {
                if (last != -1)
                    while (temp[last] < x) {
                        if (last==-1)
                            break;
                        c[y[last]] = n - i;                        
                        pop();                      
                    }                       
                func();
            }           
        }
    }
    for (i = n - 1; i >= 0; i--)
        printf("%d ", c[i]);
    return 0;
}
