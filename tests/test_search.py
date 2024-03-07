import pytest

from graph import Graph

@pytest.fixture
def my_graph():
  graph = Graph()
  graph.add_nodes(["Jasmine", "Ada", "Lydia", "Rose", "Dylan", "Allison", "Thomas", "Sarah"])
  graph.create_edges([("Jasmine", "Ada"), ("Jasmine", "Lydia"), ("Jasmine", "Rose"), ("Ada", "Dylan"), ("Lydia", "Ada"), ("Dylan", "Allison"), ("Lydia", "Thomas")])
  return graph

class Test_Depth_First:
  def test_return_false_if_target_node_does_not_exist(self, my_graph: Graph):
    assert my_graph.depthfirst_reachable("Jasmine", "Albert") == False
  
  def test_return_false_if_starting_node_does_not_exist(self, my_graph: Graph):
    assert my_graph.depthfirst_reachable("Albert", "Thomas") == False
  
  def test_check_if_first_friend_is_reachable(self, my_graph: Graph):
    assert my_graph.depthfirst_reachable("Jasmine", "Ada") == True
  
  def test_return_false_if_target_node_unreachable(self, my_graph: Graph):
    assert my_graph.depthfirst_reachable("Jasmine", "Sarah") == False

class Test_Breadth_First:
  def test_return_false_if_target_node_does_not_exist(self, my_graph: Graph):
    assert my_graph.breadthfirst_reachable("Jasmine", "Albert") == False
  
  def test_return_false_if_starting_node_does_not_exist(self, my_graph: Graph):
    assert my_graph.breadthfirst_reachable("Albert", "Thomas") == False
  
  def test_check_if_first_friend_is_reachable(self, my_graph: Graph):
    assert my_graph.breadthfirst_reachable("Jasmine", "Ada") == True
  
  def test_return_false_if_target_node_unreachable(self, my_graph: Graph):
    assert my_graph.breadthfirst_reachable("Jasmine", "Sarah") == False
