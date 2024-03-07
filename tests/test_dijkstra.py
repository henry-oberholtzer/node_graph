import pytest

from graph import Graph
from routes import cities, edges

@pytest.fixture
def vvardenfell():
  graph = Graph()
  graph.add_nodes(cities)
  graph.create_edges(edges)
  return graph

class TestDijkstra:
  def test_vivec_ebonheart(self, vvardenfell: Graph):
    assert vvardenfell.dijkstra_algorithm("Vivec", "Ebonheart") == 1
  def test_maar_gan_dagon_fel(self, vvardenfell: Graph):
    assert vvardenfell.dijkstra_algorithm("Maar Gan", "Dagon Fel") == 11
