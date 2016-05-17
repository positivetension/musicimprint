class Node:
	
	def __init__(self,val,id):
		self.val = val
		self.id = id
		self.children = []

	def addChild(self,child):
		self.children.append(child)

x = Node(4,"Nope")
y = Node(3,"Target")
z = Node(4,"Nope")
z1 = Node(4,"Nope")
z2 = Node(4,"Nope")
z3 = Node(5,"False Target")
x.addChild(z)
x.addChild(z1)
x.addChild(z2)
x.addChild(y)
z.addChild(z3)


print([chld.val for chld in x.children])

def bfs(nodelist, searchval):
	for node in nodelist:
		if node.val == searchval:
			return node
		nodelist.extend(node.children)

print(bfs([x],5).id)