import pytest

from graph import Graph

@pytest.fixture
def graph():
  return Graph()

@pytest.fixture
def vvardenfell(graph: Graph):
    node1 = "Ebonheart"
    node2 = "Vivec"
    graph.add_nodes([node1, node2])
    graph.create_edge(node1, node2, time=1, type=1)
    return graph
  

class TestGraph:
  def test_graph_initialize(self, graph: Graph):
    assert len(graph.adjacency_list) == 0
  def test_add_new_node(self, graph: Graph):
    graph.add_node("Henry")
    assert len(graph.adjacency_list.get("Henry")) == 0
  def test_false_if_node_doesnt_exist(self, graph: Graph):
    assert graph.has_node("Delaney") == False
  def test_true_if_node_exists(self, graph: Graph):
    graph.add_node("Noah")
    assert graph.has_node("Noah") == True
  def test_add_edge_between_nodes(self, graph: Graph):
    graph.add_node("Ravin")
    graph.add_node("Gabriel")
    graph.create_edge("Ravin", "Gabriel")
    assert "Gabriel" in graph.adjacency_list.get("Ravin")
    assert "Ravin" in graph.adjacency_list.get("Gabriel")
  def test_false_if_edge_doesnt_exist(self, graph: Graph):
    graph.add_node("Kim")
    graph.add_node("Teddy")
    assert graph.has_edge("Kim", "Teddy") == False
  def test_true_if_edge_exists(self, graph: Graph):
    graph.add_node("Meadow")
    graph.add_node("Met")
    graph.create_edge("Meadow", "Met")
    assert graph.has_edge("Meadow", "Met") == True
  def test_remove_edge(self, graph: Graph):
    graph.add_node("Lonnie")
    graph.add_node("Io")
    graph.create_edge("Lonnie", "Io")
    graph.remove_edge("Lonnie", "Io")
    assert graph.has_edge("Lonnie", "Io") == False
  def test_remove_node(self, graph: Graph):
    graph.add_node("Beth")
    graph.add_node("Will")
    graph.add_node("Annie")
    graph.create_edge("Will", "Annie")
    graph.create_edge("Will", "Beth")
    graph.remove_node("Will")
    assert graph.has_node("Will") == False
    assert graph.has_edge("Will", "Annie") == False
    assert graph.has_edge("Will", "Beth") == False
  def test_add_multiple_nodes(self, graph: Graph):
    names = ["Jasmine", "Ada", "Lydia"]
    graph.add_nodes(names)
    assert all([True if graph.has_node(name) else False for name in names]) == True
  def test_add_multiple_edges(self, graph: Graph):
    names = ["Jasmine", "Ada", "Lydia"]
    graph.add_nodes(names)
    edges = [("Jasmine", "Ada"), ("Ada", "Lydia"), ("Lydia", "Jasmine")]
    graph.create_edges(edges)
    assert all([True if graph.has_edge(node1, node2) else False for node1, node2, in edges])
  def test_add_weight_to_edges(self, graph: Graph):
    node1 = "Ebonheart"
    node2 = "Vivec"
    graph.add_nodes([node1, node2])
    graph.create_edge(node1, node2, time=1)
    assert graph.has_edge(node1, node2) == True
  def test_add_multiple_edges_with_weight(self, graph: Graph):
    node1 = "Ebonheart"
    node2 = "Vivec"
    graph.add_nodes([node1, node2])
    graph.create_edges([(node1, node2, 1)])
    assert graph.has_edge(node1, node2) == True
  def test_get_property_of_edge(self, vvardenfell: Graph):
    assert vvardenfell.get_prop("Ebonheart", "Vivec", "time") == 1
    assert vvardenfell.get_prop("Ebonheart", "Vivec", "type") == 1
  def test_create_directed_edge(self, graph: Graph):
    pass
    
