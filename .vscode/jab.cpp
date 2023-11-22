#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Helper function to insert elements into a binary tree using level order traversal
TreeNode* insertLevelOrder(vector<int>& values, int i, int n) {
    if (i < n) {
        if (values[i] == -1)
            return nullptr;

        TreeNode* root = new TreeNode(values[i]);

        root->left = insertLevelOrder(values, 2 * i + 1, n);
        root->right = insertLevelOrder(values, 2 * i + 2, n);

        return root;
    }
    return nullptr;
}

int maxTurns(TreeNode* root, int& max_turns) {
    if (!root)
        return 0;

    int left_turns = maxTurns(root->left, max_turns);
    int right_turns = maxTurns(root->right, max_turns);

    // Calculate turns for the current node
    int current_turns = 0;
    if ((left_turns > 0 && right_turns == 0) || (left_turns == 0 && right_turns > 0)) {
        current_turns = left_turns + right_turns + 1;
    }

    // Update the maximum turns if necessary
    max_turns = max(max_turns, current_turns);

    // Return the maximum of left and right turns
    return max(left_turns, right_turns) + 1;
}

int findMaxTurns(vector<int>& values) {
    TreeNode* root = insertLevelOrder(values, 0, values.size());
    int max_turns = 0;
    maxTurns(root, max_turns);
    return max_turns;
}

int main() {
    vector<int> values = {2, 7, 3, 5, 3, -1, 2, -1, 7, 2, 2, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1};
    int result = findMaxTurns(values);
    cout << " " << result << endl;

    return 0;
}
