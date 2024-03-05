class Graph:
  def __init__(self):
    self.adjacency_list = {}


  def add_node(self, node):
    self.adjacency_list[node] = set()

  def add_nodes(self, nodes:list):
    for node in nodes:
      self.add_node(node)
  
  def has_node(self, node):
    if self.adjacency_list.get(node) != None:
      return True
    return False
  
  def create_edge(self, node1, node2):
    self.adjacency_list.get(node1).add(node2)
    self.adjacency_list.get(node2).add(node1)
    
  def create_edges(self, edges:list):
    for node1, node2 in edges:
      self.create_edge(node1, node2)
    
  def has_edge(self, node1, node2):
    get_node1 = self.adjacency_list.get(node1)
    get_node2 = self.adjacency_list.get(node2)
    if get_node1 != None and get_node2 != None:
      if node2 in get_node1 and node1 in get_node2:
        return True
    return False
  def remove_edge(self, node1, node2):
    self.adjacency_list.get(node1).remove(node2)
    self.adjacency_list.get(node2).remove(node1)
    
  def remove_node(self, node):
    if (target_node := self.adjacency_list.get(node)) != None:
      for edge in target_node:
        self.adjacency_list.get(edge).remove(node)
      del self.adjacency_list[node]
      
  def depthfirst_reachable(self, starting_node, target_node):
    if not self.has_node(starting_node) or not self.has_node(target_node):
      return False
    stack = [starting_node]
    traversed_nodes = set()
    while stack:
      active_node = stack.pop(0)
      if (active_node == target_node):
        return True
      else:
        traversed_nodes.add(active_node)
        for node in self.adjacency_list.get(active_node):
          if node not in traversed_nodes:
            stack.insert(0, node)
    return False
            
