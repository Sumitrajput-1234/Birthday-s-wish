#include <stdio.h>

#define MAX 100

typedef struct {
    int row;
    int col;
    int value;
} Sparse;

int main() {
    Sparse sp[MAX], trans[MAX];
    int i, n;

    // Input number of non-zero elements
    printf("Enter number of non-zero elements: ");
    scanf("%d", &n);

    // Input sparse matrix in triplet form
    printf("Enter row, column, value:\n");
    for(i = 0; i <= n; i++) {
        scanf("%d %d %d", &sp[i].row, &sp[i].col, &sp[i].value);
    }

    // Transpose logic
    trans[0].row = sp[0].col;
    trans[0].col = sp[0].row;
    trans[0].value = sp[0].value;

    for(i = 1; i <= n; i++) {
        trans[i].row = sp[i].col;
        trans[i].col = sp[i].row;
        trans[i].value = sp[i].value;
    }

    // Display result
    printf("\nTranspose Sparse Matrix:\n");
    printf("Row\tCol\tValue\n");

    for(i = 0; i <= n; i++) {
        printf("%d\t%d\t%d\n", trans[i].row, trans[i].col, trans[i].value);
    }

    return 0;
}