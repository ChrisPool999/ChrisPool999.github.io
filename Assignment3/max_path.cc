#include <algorithm>
#include <iostream>

class TreeNode {
public:
  TreeNode* left = nullptr;
  TreeNode* right = nullptr;
  int val;

  TreeNode(int v) {
    val = v;
  }

  void add(TreeNode* root, TreeNode* new_node) {
    while (true) {
      bool goleft = (new_node->val < root->val);

      if (goleft && !root->left) {
        root->left = new_node;
        return;
      }
      else if (!goleft && !root->right) {
        root->right = new_node;
        return;
      }

      root = (goleft ? root->left : root->right);
    }
  }
};

int max_path_helper(TreeNode* root, int& best) {
  if (!root) return 0;

  int left = std::max(0, max_path_helper(root->left, best));
  int right = std::max(0, max_path_helper(root->right, best));

  int path = left + right + root->val;
  if (path > best) {
    best = path;
  }

  return std::max(left, right) + root->val;
}

int max_path(TreeNode* root) {
  if (!root) {
    return 0;
  }

  int result = root->val;
  max_path_helper(root, result);
  return result;
}

int main() {
  // NORMAL CASE
  TreeNode* TEST_1 = new TreeNode(2);
  TreeNode* node = new TreeNode(6);
  TEST_1->add(TEST_1, node);
  node = new TreeNode(8);
  TEST_1->add(TEST_1, node);
  node = new TreeNode(4);
  TEST_1->add(TEST_1, node);
  node = new TreeNode(-2);
  TEST_1->add(TEST_1, node);
  node = new TreeNode(0);
  TEST_1->add(TEST_1, node);
  std::cout << max_path(TEST_1) << std::endl;

  // NORMAL CASE
  TreeNode* TEST_2 = new TreeNode(1);
  node = new TreeNode(2);
  TEST_2->add(TEST_2, node);
  node = new TreeNode(3);
  TEST_2->add(TEST_2, node);
  std::cout << max_path(TEST_2) << std::endl;

  // CHECK ALL NEGATIVE
  TreeNode* TEST_3 = new TreeNode(-30);
  node = new TreeNode(-10);
  TEST_2->add(TEST_3, node);
  node = new TreeNode(-20);
  TEST_2->add(TEST_3, node);
  node = new TreeNode(-15);
  TEST_2->add(TEST_3, node);
  node = new TreeNode(-7);
  TEST_2->add(TEST_3, node);
  std::cout << max_path(TEST_3) << std::endl;

  // CHECK SIZE 0
  TreeNode* TEST_4 = nullptr;
  std::cout << max_path(TEST_4) << std::endl;  

  // CHECK SIZE 1
  TreeNode* TEST_5 = new TreeNode(9);
  std::cout << max_path(TEST_5) << std::endl;
}

