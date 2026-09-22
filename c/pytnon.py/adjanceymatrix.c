#include <stdio.h>

#define MAX 100

int main() {
    int adj[MAX][MAX];
    int n, i, j, edges;
    int u, v;

    // Input number of vertices
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    // Initialize adjacency matrix to 0
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            adj[i][j] = 0;
        }
    }

    // Input number of edges
    printf("Enter number of edges: ");
    scanf("%d", &edges);

    // Input edges
    printf("Enter edges (u v) format (0-based index):\n");
    for(i = 0; i < edges; i++) {
        scanf("%d %d", &u, &v);

        // For undirected graph
        adj[u][v] = 1;
        adj[v][u] = 1;

        // For directed graph, comment above line and use:
        // adj[u][v] = 1;
    }

    // Display adjacency matrix
    printf("\nAdjacency Matrix:\n");
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            printf("%d ", adj[i][j]);
        }
        printf("\n");
    }

    return 0;
}