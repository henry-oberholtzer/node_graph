import pytest

from graph import Graph

class Test_Breadth_First:
  @pytest.fixture
  def graph():
    graph = Graph()
    graph.add_nodes(["Jasmine", "Ada", "Lydia", "Rose", "Dylan", "Allison", "Thomas", "Sarah"])
    graph.create_edges([("Jasmine", "Ada"), ("Jasmine", "Lydia"), ("Jasmine", "Rose"), ("Ada", "Dylan"), ("Lydia", "Ada"), ("Dylan", "Allison"), ("Lydia", "Thomas")])
    return graph
  
