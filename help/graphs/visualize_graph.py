import graphviz

g = graphviz.Digraph('G', filename='graph.gv')



g.edge('a', 'd')
g.edge('a', 'f')
g.edge('a', 's')
g.edge('s', 'd')


g.view()