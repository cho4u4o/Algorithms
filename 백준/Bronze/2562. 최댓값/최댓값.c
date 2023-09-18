#include <stdio.h>

int main() {
    int array[9];
    int max_num = 0;
    int index = 0;

    for (int i = 0; i < 9; i++) {
        scanf("%d", &array[i]);
        max_num = max_num < array[i] ? array[i] : max_num;
        index = array[i] == max_num ? i : index;
    }

    printf("%d\n", max_num);
    printf("%d", index + 1);
    return 0;
}