#include <stdio.h>

#define MAX 100

// Function to read sparse matrix
void readSparse(int a[MAX][3]) {
    int i;
    printf("Enter number of rows, columns and non-zero elements: ");
    scanf("%d %d %d", &a[0][0], &a[0][1], &a[0][2]);

    printf("Enter row, column, value:\n");
    for (i = 1; i <= a[0][2]; i++) {
        scanf("%d %d %d", &a[i][0], &a[i][1], &a[i][2]);
    }
}

// Function to display sparse matrix
void display(int a[MAX][3]) {
    int i;
    printf("\nRow Col Val\n");
    for (i = 0; i <= a[0][2]; i++) {
        printf("%d %d %d\n", a[i][0], a[i][1], a[i][2]);
    }
}

// Function to transpose sparse matrix
void transpose(int a[MAX][3], int t[MAX][3]) {
    int i, j, k = 1;

    t[0][0] = a[0][1];
    t[0][1] = a[0][0];
    t[0][2] = a[0][2];

    for (i = 0; i < a[0][1]; i++) {
        for (j = 1; j <= a[0][2]; j++) {
            if (a[j][1] == i) {
                t[k][0] = a[j][0];
                t[k][1] = a[j][1];
                t[k][2] = a[j][2];
                k++;
            }
        }
    }
}

// Function to multiply two sparse matrices
void multiply(int a[MAX][3], int b[MAX][3], int res[MAX][3]) {
    int i, j, k = 1;
    int sum;

    if (a[0][1] != b[0][0]) {
        printf("Multiplication not possible!\n");
        return;
    }

    res[0][0] = a[0][0];
    res[0][1] = b[0][1];

    for (i = 0; i < a[0][0]; i++) {
        for (j = 0; j < b[0][1]; j++) {
            sum = 0;
            for (int p = 1; p <= a[0][2]; p++) {
                for (int q = 1; q <= b[0][2]; q++) {
                    if (a[p][0] == i && b[q][1] == j && a[p][1] == b[q][0]) {
                        sum += a[p][2] * b[q][2];
                    }
                }
            }
            if (sum != 0) {
                res[k][0] = i;
                res[k][1] = j;
                res[k][2] = sum;
                k++;
            }
        }
    }
    res[0][2] = k - 1;
}

// Main function
int main() {
    int A[MAX][3], B[MAX][3], BT[MAX][3], RESULT[MAX][3];

    printf("Enter first sparse matrix:\n");
    readSparse(A);

    printf("Enter second sparse matrix:\n");
    readSparse(B);

    printf("\nFirst Matrix:");
    display(A);

    printf("\nSecond Matrix:");
    display(B);

    // Transpose of second matrix
    transpose(B, BT);

    printf("\nTranspose of Second Matrix:");
    display(BT);

    // Multiply A with Transpose(B)
    multiply(A, BT, RESULT);

    printf("\nResult (A * Transpose(B)):");
    display(RESULT);

    return 0;
}