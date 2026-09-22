// #include <stdio.h>
// #include <stdlib.h>

// // Node structure
// typedef struct Node {
//     int key;
//     struct Node *left;
//     struct Node *right;
//     int height;
// } Node;

// // Utility function to get height
// int height(Node *n) {
//     if (n == NULL)
//         return 0;
//     return n->height;
// }

// // Utility to get max of two numbers
// int max(int a, int b) {
//     return (a > b) ? a : b;
// }

// // Create a new node
// Node* newNode(int key) {
//     Node* node = (Node*)malloc(sizeof(Node));
//     node->key = key;
//     node->left = node->right = NULL;
//     node->height = 1;
//     return node;
// }

// // Right rotation
// Node* rightRotate(Node *y) {
//     Node *x = y->left;
//     Node *T2 = x->right;

//     // Perform rotation
//     x->right = y;
//     y->left = T2;

//     // Update heights
//     y->height = max(height(y->left), height(y->right)) + 1;
//     x->height = max(height(x->left), height(x->right)) + 1;

//     return x;
// }

// // Left rotation
// Node* leftRotate(Node *x) {
//     Node *y = x->right;
//     Node *T2 = y->left;

//     // Perform rotation
//     y->left = x;
//     x->right = T2;

//     // Update heights
//     x->height = max(height(x->left), height(x->right)) + 1;
//     y->height = max(height(y->left), height(y->right)) + 1;

//     return y;
// }

// // Get balance factor
// int getBalance(Node *n) {
//     if (n == NULL)
//         return 0;
//     return height(n->left) - height(n->right);
// }

// // Insert node
// Node* insert(Node* node, int key) {
//     // Normal BST insertion
//     if (node == NULL)
//         return newNode(key);

//     if (key < node->key)
//         node->left = insert(node->left, key);
//     else if (key > node->key)
//         node->right = insert(node->right, key);
//     else
//         return node; // No duplicates

//     // Update height
//     node->height = 1 + max(height(node->left), height(node->right));

//     // Get balance factor
//     int balance = getBalance(node);

//     // Balance cases

//     // Left Left
//     if (balance > 1 && key < node->left->key)
//         return rightRotate(node);

//     // Right Right
//     if (balance < -1 && key > node->right->key)
//         return leftRotate(node);

//     // Left Right
//     if (balance > 1 && key > node->left->key) {
//         node->left = leftRotate(node->left);
//         return rightRotate(node);
//     }

//     // Right Left
//     if (balance < -1 && key < node->right->key) {
//         node->right = rightRotate(node->right);
//         return leftRotate(node);
//     }

//     return node;
// }

// // Preorder traversal
// void preOrder(Node *root) {
//     if (root != NULL) {
//         printf("%d ", root->key);
//         preOrder(root->left);
//         preOrder(root->right);
//     }
// }

// // Main function
// int main() {
//     Node *root = NULL;

//     root = insert(root, 10);
//     root = insert(root, 20);
//     root = insert(root, 30);
//     root = insert(root, 40);
//     root = insert(root, 50);
//     root = insert(root, 25);

//     printf("Preorder traversal of AVL tree:\n");
//     preOrder(root);

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int key;
    struct Node *left;
    struct Node *right;
    int height;
};

// Utility function to get height of a node
int height(struct Node *N) {
    if (N == NULL)
        return 0;
    return N->height;
}

// Utility function to get maximum of two integers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Create a new node
struct Node* newNode(int key) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1; // new node is initially added at leaf
    return node;
}

// Right rotate subtree rooted with y
struct Node* rightRotate(struct Node* y) {
    struct Node* x = y->left;
    struct Node* T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    // Return new root
    return x;
}

// Left rotate subtree rooted with x
struct Node* leftRotate(struct Node* x) {
    struct Node* y = x->right;
    struct Node* T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights
    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    // Return new root
    return y;
}

// Get balance factor of node N
int getBalance(struct Node* N) {
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}

// Insert a key into the AVL tree
struct Node* insert(struct Node* node, int key) {
    // Normal BST insertion
    if (node == NULL)
        return newNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else // Equal keys not allowed
        return node;

    // Update height
    node->height = 1 + max(height(node->left), height(node->right));

    // Get balance factor
    int balance = getBalance(node);

    // Balance the tree
    // Left Left Case
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

// Utility function to find minimum value node
struct Node* minValueNode(struct Node* node) {
    struct Node* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}

// Delete a node
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL)
        return root;

    // Perform standard BST delete
    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        // Node with one child or no child
        if ((root->left == NULL) || (root->right == NULL)) {
            struct Node* temp = root->left ? root->left : root->right;

            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else
                *root = *temp; // Copy contents

            free(temp);
        } else {
            // Node with two children
            struct Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (root == NULL)
        return root;

    // Update height
    root->height = 1 + max(height(root->left), height(root->right));

    // Get balance factor
    int balance = getBalance(root);

    // Balance the tree
    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

// Preorder traversal
void preOrder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->key);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// Driver program
int main() {
    struct Node* root = NULL;

    // Insert nodes
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    printf("Preorder traversal of AVL tree:\n");
    preOrder(root);

    root = deleteNode(root, 40);

    printf("\nPreorder traversal after deletion of 40:\n");
    preOrder(root);

    return 0;
}
