#include <vector>
#include <iostream>

using vec = std::vector<int>;
using vec2D = std::vector<std::vector<int>>;

void all_paths_helper(vec2D& graph, int node, vec2D& output, vec& curr) {
    curr.push_back(node);

    if (node == graph.size() - 1) {
        output.push_back(curr);
        return;
    }
    if (!graph[node].size()) return;

    for (int i = 1; i < graph[node].size(); i++) {
        vec copy = curr;
        all_paths_helper(graph, graph[node][i], output, copy); 
    }
    all_paths_helper(graph, graph[node][0], output, curr); 
}

vec2D all_paths(vec2D& graph) {
    vec2D output = {};
    vec start = {};
    all_paths_helper(graph, 0, output, start);
    return output;
}

int main() {
  // BASIC
  std::cout << "BASIC" << std::endl;
  vec2D graph = {{4,3,1},{3,2,4},{3},{4},{}};

  for (vec& v : all_paths(graph)) {
    for (int n : v) {
      std::cout << n << " "; // expects: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    }
    if (!v.size()) {
      std::cout << "None ";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;

  // ONE SINGLE PATH
  std::cout << "ONE SINGLE PATH" << std::endl;
  graph = {{1},{2},{3},{}};
  for (vec& v : all_paths(graph)) { 
    for (int n : v) {
      std::cout << n << " "; // expects: [[0, 1, 2, 3]]
    }
    if (!v.size()) {
      std::cout << "None ";
    } 
    std::cout << std::endl;
  } 

  std::cout << std::endl;

  // NO PATH
  std::cout << "NO PATH" << std::endl;
  graph = {{1, 2},{2},{3},{}, {}};
  for (vec& v : all_paths(graph)) { 
    for (int n : v) {
      std::cout << n << " "; // expects: []
    }
    if (!v.size()) {
      std::cout << "None ";
    } 
    std::cout << std::endl;
  } 

  std::cout << std::endl;

  // ALL EMPTY
  std::cout << "ALL EMPTY" << std::endl;
  graph = {{},{},{},{}, {}};
  for (vec& v : all_paths(graph)) { 
    for (int n : v) {
      std::cout << n << " "; // expects: []
    }
    if (!v.size()) {
      std::cout << "None ";
    } 
    std::cout << std::endl;
  } 

  std::cout << std::endl;

  // N - 1 CONTAINS PATHS
  std::cout << "N - 1 Contains Paths" << std::endl;
  graph = {{2},{},{1}};
  for (vec& v : all_paths(graph)) { 
    for (int n : v) {
      std::cout << n << " "; // expects: [[0, 2]]
    }
    if (!v.size()) {
      std::cout << "None ";
    } 
    std::cout << std::endl;
  }  

  return 0;
}