#include <vector>
#include <iostream>
#include <unordered_map>

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

// for checking test cases
void inorder_traversal(TreeNode* root) {
  if (!root) {
    std::cout << "null" << std::endl;
    return;
  }

  std::cout << root->val << std::endl;
  inorder_traversal(root->left);
  inorder_traversal(root->right);
}

TreeNode* tree_recursion(std::vector<int>& preorder, int& index,
      std::unordered_map<int, int>& inorder_postions, int lower_bounds = -1, int upper_bounds = -1) {

  if (index >= preorder.size()) return nullptr;

  int next = preorder[index];
  bool OOB_left = (lower_bounds != -1 and inorder_postions[next] < lower_bounds);
  bool OOB_right = (upper_bounds != -1 and inorder_postions[next] > upper_bounds);

  if (OOB_left || OOB_right) return nullptr;
  
  TreeNode* node = new TreeNode(next);
  index++;

  // boundaries check example: root = root->left, now ALL children must be lower than that root
  node->left = tree_recursion(preorder, index, inorder_postions, lower_bounds, inorder_postions[next]);
  node->right = tree_recursion(preorder, index, inorder_postions, inorder_postions[next], upper_bounds);

  return node;
}

TreeNode* construct_tree(std::vector<int>& inorder, std::vector<int>& preorder) {
  // inorder tells us if a node is left or right of a root
  std::unordered_map<int, int> inorder_postions;
  for (int i = 0; i < inorder.size(); i++) {
    inorder_postions[inorder[i]] = i;
  }

  int index = 0;
  return tree_recursion(preorder, index, inorder_postions);
}

int main() {
  std::vector<int> preorder = {3,9,20,15,7};
  std::vector<int> inorder = {9,3,15,20,7};
  TreeNode* TEST_1 = construct_tree(inorder, preorder);
  inorder_traversal(TEST_1);
  std::cout << "\n";

  preorder = {-1};
  inorder = {-1};
  TreeNode* TEST_2 = construct_tree(inorder, preorder);
  inorder_traversal(TEST_2);
  std::cout << "\n";
}