// #include <stdio.h>
// #include <stdlib.h>

// // Define node structure
// struct Node {
//     int data;
//     struct Node* left;
//     struct Node* right;
// };

// // Create a new node
// struct Node* createNode(int value) {
//     struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
//     newNode->data = value;
//     newNode->left = NULL;
//     newNode->right = NULL;
//     return newNode;
// }

// // Insert a node into BST
// struct Node* insert(struct Node* root, int value) {
//     if (root == NULL) {
//         return createNode(value);
//     }

//     if (value < root->data) {
//         root->left = insert(root->left, value);
//     } else if (value > root->data) {
//         root->right = insert(root->right, value);
//     }

//     return root;
// }

// // Search in BST
// struct Node* search(struct Node* root, int key) {
//     if (root == NULL || root->data == key) {
//         return root;
//     }

//     if (key < root->data) {
//         return search(root->left, key);
//     } else {
//         return search(root->right, key);
//     }
// }

// // Inorder Traversal (Left, Root, Right)
// void inorder(struct Node* root) {
//     if (root != NULL) {
//         inorder(root->left);
//         printf("%d ", root->data);
//         inorder(root->right);
//     }
// }

// // Main function
// int main() {
//     struct Node* root = NULL;

//     // Insert nodes
//     root = insert(root, 50);
//     insert(root, 30);
//     insert(root, 70);
//     insert(root, 20);
//     insert(root, 40);
//     insert(root, 60);
//     insert(root, 80);

//     printf("Inorder traversal: ");
//     inorder(root);

//     // Search for a value
//     int key = 40;
//     struct Node* result = search(root, key);

//     if (result != NULL) {
//         printf("\n%d found in BST.\n", key);
//     } else {
//         printf("\n%d not found in BST.\n", key);
//     }

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

// Node structure for BST
struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* newNode(int key) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->key = key;
    node->left = node->right = NULL;
    return node;
}

// Function to insert a node in BST
struct Node* insert(struct Node* root, int key) {
    if (root == NULL) {
        return newNode(key);
    }
    if (key < root->key) {
        root->left = insert(root->left, key);
    } else if (key > root->key) {
        root->right = insert(root->right, key);
    }
    return root; // unchanged if key already exists
}

// Function to find the minimum value node in BST
struct Node* findMin(struct Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Function to delete a node from BST
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) return root;

    if (key < root->key) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->key) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node found
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        } else {
            // Node with two children
            struct Node* temp = findMin(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }
    return root;
}

// Inorder traversal (sorted order)
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

int main() {
    struct Node* root = NULL;

    // Insert nodes
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);

    printf("Inorder traversal of BST: ");
    inorder(root);
    printf("\n");

    // Delete nodes
    root = deleteNode(root, 20);
    printf("After deleting 20: ");
    inorder(root);
    printf("\n");

    root = deleteNode(root, 50);
    printf("After deleting 50: ");
    inorder(root);
    printf("\n");

    return 0;
}

