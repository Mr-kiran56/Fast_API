# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# data_map = {}

# def build_tree(preorder, inorder):
#     if not preorder or not inorder:
#         return None
    
#     root_val = preorder[0]          
#     root_index = inorder.index(root_val) 
    
#     # Left and right parts of inorder
#     left_inorder = inorder[:root_index]
#     right_inorder = inorder[root_index + 1:]
    
#     # Left and right parts of preorder
#     left_preorder = preorder[1:1 + len(left_inorder)]
#     right_preorder = preorder[1 + len(left_inorder):]
    
#     # Add to data_map
#     data_map[root_val] = {
#         'left': left_preorder[0] if left_preorder else None,
#         'right': right_preorder[0] if right_preorder else None
#     }
    
#     # Recursively process left and right
#     build_tree(left_preorder, left_inorder)
#     build_tree(right_preorder, right_inorder)

# build_tree(preorder, inorder)
# print(data_map)

def countval(n):
    if n==0:
        return 1
    count=0
    while n>0:
        n//=10
        count+=1
    return count
print(countval(100))



