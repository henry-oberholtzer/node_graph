import pytest

from graph import Graph

@pytest.fixture
def graph():
  return Graph()
