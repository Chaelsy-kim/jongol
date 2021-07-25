#include <stdio.h>
int a[80000] = { 0 };
int top = -1;

int pop() {
    return a[top--];
}

void push(int x) {
    a[++top] = x;
}
int main() {

    int i, n, x;
    unsigned int sum = 0;

    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        scanf("%d", &x);

        if(top==-1)
            push(x);
        else {
            if (a[top] > x) 
                push(x);
            else {
                while (a[top] <= x) {
                    if (top == -1)
                        break;
                    pop();
                }                    
                push(x);   
            }
            sum += top;
        }

    }

    printf("%u", sum);

    return 0;
}
