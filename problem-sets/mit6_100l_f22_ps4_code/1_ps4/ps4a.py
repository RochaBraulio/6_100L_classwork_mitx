# Problem Set 4A
# Name: Braulio Rocha
# Collaborators: None

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

tr1 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11))) # True
tr2 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1)))) # False

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    height = 0
    if tree.get_left_child() is None and tree.get_right_child() is None:
        height = 0 # height of leaf node is zero
    elif tree.get_left_child() is None:
        height = find_tree_height(tree.get_right_child()) + 1
    elif tree.get_right_child() is None:
        height = find_tree_height(tree.get_left_child()) + 1
    else:
        height = max(
            find_tree_height(tree.get_left_child()),
            find_tree_height(tree.get_right_child())) + 1 
    return height   

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree.get_left_child() is None and tree.get_right_child() is None:
        return True # base case for leaf node
    elif tree.get_left_child() is None:
        heap_check_right = (
            compare_func(
                tree.get_right_child().get_value(),
                tree.get_value()
                )
            and is_heap(tree.get_right_child(),compare_func)
            )
        return heap_check_right
    elif tree.get_right_child() is None:
        heap_check_left = (
            compare_func(
                tree.get_left_child().get_value(),
                tree.get_value()
                )
            and is_heap(tree.get_left_child(),compare_func)
            )
        return heap_check_left
    else:
        # checks if left subtree is a heap
        heap_check_left = (
            compare_func(
                tree.get_left_child().get_value(),
                tree.get_value()
                )
            and is_heap(tree.get_left_child(),compare_func)
            )
        # checks if right subtree is a heap
        heap_check_right = (
            compare_func(
                tree.get_right_child().get_value(),
                tree.get_value()
                )
            and is_heap(tree.get_right_child(),compare_func)
            )
        return (heap_check_left and heap_check_right)

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
