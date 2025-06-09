# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        ans = ""
        q = [root]
        
        while q:
            curr_level = ""
            
            for _ in range(len(q)):
                curr = q.pop(0)
                
                if curr:
                    curr_level += str(curr.val) + ","
                    
                    q.append(curr.left)
                    q.append(curr.right)
                    
                else:
                    curr_level += "N,"
            
            ans += curr_level
        
        return ans
            
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q = [root]
        i = 1
        
        while q and i < len(data):
            node = q.pop(0)
            
            if data[i] != 'N':
                left = TreeNode(int(data[i]))
                node.left = left
                q.append(left)
            i += 1
            
            if data[i] != 'N':
                right = TreeNode(int(data[i]))
                node.right = right
                q.append(right)
            i += 1
            
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))