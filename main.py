from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while frontier:
        current_node = frontier.pop()
        for neighbor in graph[current_node]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result

def connected(graph):
    """
    Determines if the graph is connected.
    """
    if not graph:
        return True
    start_node = next(iter(graph))  # Get any starting node
    reached_nodes = reachable(graph, start_node)
    return len(reached_nodes) == len(graph)

def n_components(graph):
    """
    Returns the number of connected components in an undirected graph.
    """
    seen = set()
    components = 0
    for node in graph:
        if node not in seen:
            reached = reachable(graph, node)
            seen.update(reached)
            components += 1
    return components