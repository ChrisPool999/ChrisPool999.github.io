#include <algorithm>
#include <iostream>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

int max_path(TreeNode* root, int& result) {
  if (!root) {
    return 0;
  }

  int left = std::max(0, max_path(root->left, result)); 
  int right = std::max(0, max_path(root->right, result));
  
  result = std::max(result, left + right + root->val);

  return std::max(left, right) + root->val;
}

int max_path(TreeNode* root) {
  if (!root) {
    return 0;
  }

  int result = root->val;
  max_path(root, result);
  return result;
}

int main() {
  // basic
  TreeNode* root = new TreeNode(6, new TreeNode(4), new TreeNode(9));
  std::cout << (max_path(root)) << std::endl;

  // size 1
  root = new TreeNode(8);
  std::cout << (max_path(root)) << std::endl;

  // size 0
  root = nullptr;
  std::cout << (max_path(root)) << std::endl;

  // all negative
  root = new TreeNode(-6, new TreeNode(-4), new TreeNode(-9));
  std::cout << (max_path(root)) << std::endl;

  // bigger size + with negative paths
  TreeNode* left = new TreeNode(4, new TreeNode(-4), new TreeNode(5));
  TreeNode* right = new TreeNode(10, new TreeNode(8), nullptr);
  root = new TreeNode(6, left, right);
  std::cout << (max_path(root)) << std::endl;
}