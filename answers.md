# CMPS 2200 Recitation 10## Answers

**Name:**___Raymond Liu______________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work of the `reachable` function, given a graph with \(n\) nodes and \(m\) edges, is \(O(n + m)\). This accounts for visiting each node once and checking all edges connected to nodes in the frontier.
- **4)**
In the context of determining if an undirected graph is connected, the worst-case number of times the reachable function needs to be called is once. This is because to check for connectivity in a graph, one effective approach is to select any node as a starting point and see if all other nodes in the graph can be reached from this node using the reachable function. If all nodes are indeed reachable from this selected node, then the graph is connected; if not, it is disconnected. Thus, only one execution of reachable is required to determine the connectivity of the entire graph.
- **5)**
The work of the connected function, when we have a graph with n nodes and m edges, can be described using the Big O notation. The connected function checks whether all nodes in a graph are reachable from a given start node. This involves calling the reachable function once, which has a work of O(n+m) because it needs to explore all nodes and all edges in the worst case. Therefore, the total work of the connected function is also O(n+m), as it relies solely on a complete traversal of the graph using the reachable function from a single starting node.
- **7)**
Switching the graph representation to an adjacency matrix affects the work of the reachable function. In an adjacency matrix, the function would need to check all possible connections for each node, leading to a time complexity of O(n^2), where n is the number of nodes. This is because, regardless of the actual number of edges, the algorithm must inspect every possible pair of nodes to determine connectivity.