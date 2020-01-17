
'''

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2    4
 \ /   / | \
  3   5  8  9
   \ / \     \
    6   7    11


Sample input/output (pseudodata):

parentChildPairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]


     
    
Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.


Output may be in any order:


findNodesWithZeroAndOneParents(parentChildPairs) => [
  [1, 2, 4],       // Individuals with zero parents
  [5, 7, 8, 9, 11] // Individuals with exactly one parent
]

'''

def avoid_same_node(current, each):
    return not (current[1] == each[1] and current[0] == each[0])

def have_parent(current_parent,parent_child_pairs):
    for node in parent_child_pairs:
        if current_parent == node[1] and node[0] != current_parent:
            return True    
    return False
        
def findNodesWithZeroAndOneParents(parent_child_pairs): # O(n^2), send a PR if you know how to improve =)
    # 0 for parent
    # 1 for children
    zero_parent = [] 
    one_parent = []
    for root_node in parent_child_pairs:
        unique_parent = True
        counter_parent_ocurrences = 0
        for each_node in parent_child_pairs:
            if avoid_same_node(root_node, each_node):
                # current root does not have parent node 
                if root_node[0] == each_node[0] and root_node[0] == each_node[1]:
                    unique_parent = False
                # current root node is child of some other node
                if root_node[0] == each_node[1] and root_node[1] == each_node[0]:
                    counter_parent_ocurrences += 1
                # current node has same child than other node but different parent
                if root_node[1] == each_node[1] and root_node[0] != each_node[0]: 
                    counter_parent_ocurrences += 1
                    
        if unique_parent:
            if not have_parent(root_node[0],parent_child_pairs):
                if len(zero_parent) == 0:
                    zero_parent.append(root_node[0])
                elif not root_node[0] in zero_parent:
                    zero_parent.append(root_node[0])
        if counter_parent_ocurrences == 0:
            if len(one_parent) == 0:
                one_parent.append(root_node[1])
            elif not root_node[1] in one_parent:
                one_parent.append(root_node[1])
    return [zero_parent,one_parent]
                        
                
    
parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

result = findNodesWithZeroAndOneParents(parent_child_pairs)
print(result)
