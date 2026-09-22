#include <stdio.h>

#define MAX 100

typedef struct {
    int row;
    int col;
    int value;
} Sparse;

int main() {
    int m, n, i, j, k = 1;
    int matrix[10][10];
    Sparse sp[MAX];

    printf("Enter number of rows and columns: ");
    scanf("%d %d", &m, &n);

    printf("Enter matrix elements:\n");
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Convert to sparse form
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            if(matrix[i][j] != 0) {
                sp[k].row = i;
                sp[k].col = j;
                sp[k].value = matrix[i][j];
                k++;
            }
        }
    }

    // First element stores metadata
    sp[0].row = m;
    sp[0].col = n;
    sp[0].value = k - 1;

    // Display sparse matrix
    printf("\nSparse Matrix (Triplet Form):\n");
    printf("Row\tCol\tValue\n");

    for(i = 0; i < k; i++) {
        printf("%d\t%d\t%d\n", sp[i].row, sp[i].col, sp[i].value);
    }

    return 0;
}