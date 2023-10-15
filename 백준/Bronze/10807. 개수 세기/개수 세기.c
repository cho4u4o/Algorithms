#include <stdio.h>

int main () {
    int n = 0;
    int num, cnt = 0;
    scanf("%d", &n);
    int arr[100] = {0};

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    scanf("%d", &num);

    for (int i = 0; i < n; i++) {
        if (arr[i] == num)
            cnt++;
    }

    printf("%d", cnt);
    return 0;
}