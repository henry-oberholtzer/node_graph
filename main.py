# Copyright (C) 2024 Henry Oberholtzer

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from pytest import main

from graph import Graph

from routes import cities, edges

vvardenfell = Graph()

vvardenfell.add_nodes(cities)
vvardenfell.create_edges(edges)
print(vvardenfell.adjacency_list)
print("Hla Oad to Caldera: ", vvardenfell.depthfirst_reachable("Hla Oad", "Caldera"))
print("Seyda Neen to Vivec: ", vvardenfell.breadthfirst_reachable("Seyda Neen", "Vivec"))

main(['-vv'])
