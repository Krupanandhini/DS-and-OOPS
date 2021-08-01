class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
     
a1=BinaryTreeNode(10)
a2=BinaryTreeNode(15)
a3=BinaryTreeNode(20)

a1.leftChild=a2
a1.rightChild=a3

print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)

'''output
Root Node is:
10
left child of node is:
15
right child of node is:
20'''