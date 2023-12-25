import graphviz

g = graphviz.Digraph('G', filename='hello.gv')




g.edge('Hello', 'World')


g.view()



for line in data:
	a, b = line.split(': ')
	b = b.split()
	for c in b:
		g.edge(a,c)

g.view()