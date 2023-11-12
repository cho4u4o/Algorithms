#include <stdio.h>

int main () {
    int n = 0;
    int arr[46] = {0}; // 순서별 피보나치 수를 저장할 배열
    int *p = arr + 2; // 시작 포인터의 주소를 arr[2]로 설정

    arr[0] = 0; arr[1] = 1; // 0번째, 1번째 피보나치 수를 0과 1로 설정
    scanf("%d", &n); // n을 입력받는다

    for (int i = 2; i < (n + 1); i++) {
        *p = *(p-2) + *(p-1);
        p = p + 1;
    }
    printf("%d", arr[n]);

    return 0;
}