class Node:

  def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None

def solution(root):
  findMaxSum.max = -999
  findMaxSum(root)
  return findMaxSum.max

def findMaxSum(root):
  if root is None:
    return 0
  l_max = findMaxSum(root.left)
  r_max = findMaxSum(root.right)
  one_side_max = max(root.val, root.val + max(r_max, l_max))

  max_top = max(one_side_max, l_max + root.val + r_max) # max sum with parent node if exist
  findMaxSum.max = max(max_top, findMaxSum.max) # here to store real max path sum
  return one_side_max # return only one side of path sum, for level above to sum this side + parent node


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
