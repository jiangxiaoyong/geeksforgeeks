class Node:

  def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None

def solution(root):
  if root is None:
    return True

  if root.left is None and root.right is None:
    return True

  if root.left is not None and root.right is not None:
    return solution(root.left) and solution(root.right)

  return False



root = Node(10)
root.left = Node(2)
root.left.left = Node(20)
root.left.right = Node(1)
root.right = Node(10)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)



#     10
#    / \
#   2   10
#  /\     \
# 20 1    -25
#          / \
#          3  4
