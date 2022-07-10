class Node:
	def __init__(self, data):
		self.dataVal = data
		self.nextVal = None


class LinkedList:
	def __init__(self):
		self.headVal = None


def findTotal(lis):
	return addRecursively(lis.headVal)


def addRecursively(node):
	if node.nextVal is None:
		return node.dataVal
	else:
		return node.dataVal + addRecursively(node.nextVal)


def addLast(lis, addnode):
	node = moveToLastRecursively(lis.headVal)
	node.nextVal = addnode
	return findTotal(lis)


def moveToLastRecursively(node):
	if node.nextVal is None:
		return node
	else:
		return moveToLastRecursively(node.nextVal)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.nextVal = node2
node2.nextVal = node3


list1 = LinkedList()
list1.headVal = node1


print("total of list before adding fourth node : ", findTotal(list1))
print("total of list after adding fourth node : ", addLast(list1, node4))



